"""Code Nexus - Data Processor.

Defines an abstract ``DataProcessor`` interface and three concrete
processors (numeric, text, log) that each know how to validate and
ingest their own kind of data, while sharing the same public API.
This is a classic example of polymorphism through an Abstract Base
Class (ABC): calling code only ever talks to a ``DataProcessor``,
never needing to know which subclass it actually holds.
"""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Common interface for every data processor of the Code Nexus.

    Subclasses must implement ``validate`` and ``ingest``. Both the
    internal storage and the ``output`` method are shared by every
    subclass, so the FIFO (first-in, first-out) behaviour and the
    ranking of items is identical no matter what kind of data is
    being processed.
    """

    def __init__(self) -> None:
        # Each stored item is a (rank, text) pair. Rank records the
        # order items were ingested in, independent of their type.
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Tell whether this processor can ingest the provided data."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process the data and store it, keeping each item separated."""
        pass

    def output(self) -> tuple[int, str]:
        """Pop the oldest stored item along with its processing rank."""
        if not self._storage:
            raise IndexError("No data left to output")

        # list.pop(0) removes and returns the first element, which is
        # the oldest one since _store always appends at the end.
        return self._storage.pop(0)

    def _store(self, item: str) -> None:
        """Append one processed item and give it the next rank."""
        self._storage.append((self._rank, item))
        self._rank += 1


class NumericProcessor(DataProcessor):
    """Processes single numbers or lists of numbers (int/float)."""

    def validate(self, data: Any) -> bool:
        """Accept an int, a float, or a list made only of int/float.

        ``bool`` is explicitly excluded even though Python treats it
        as a subclass of ``int`` (``isinstance(True, int)`` is
        ``True``). Without this check, booleans would silently be
        accepted as numeric data.
        """
        if isinstance(data, bool):
            return False

        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            # all(...) is False as soon as one item fails the test,
            # so a single bad element invalidates the whole list.
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        """Validate then store each number as a string."""
        if not self.validate(data):
            # Guards against callers who skip validate() before
            # calling ingest() with data of the wrong shape/type.
            raise TypeError("Improper numeric data")

        # Normalize a single value into a one-item list so the loop
        # below can treat "one number" and "many numbers" the same.
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(str(item))


class TextProcessor(DataProcessor):
    """Processes a single string or a list of strings."""

    def validate(self, data: Any) -> bool:
        """Accept a string, or a list made only of strings."""
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        """Validate then store each string as-is."""
        if not self.validate(data):
            raise TypeError("Improper text data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(item)


class LogProcessor(DataProcessor):
    """Processes a single log entry or a list of log entries.

    A log entry is a ``dict`` whose keys and values are all strings,
    e.g. ``{'log_level': 'ERROR', 'log_message': 'Boom'}``.
    """

    def _is_log(self, data: Any) -> bool:
        """Check that ``data`` is a dict of str keys to str values."""
        return isinstance(data, dict) and all(
            isinstance(k, str) and isinstance(v, str) for k, v in data.items()
        )

    def validate(self, data: Any) -> bool:
        """Accept one log entry, or a list of log entries."""
        if isinstance(data, list):
            return all(self._is_log(item) for item in data)

        return self._is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        """Validate then flatten each log entry into one string."""
        if not self.validate(data):
            raise TypeError("Improper log data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            # Join only the values (e.g. "ERROR" and "Boom"), not the
            # keys, so the stored text reads like a real log line.
            self._store(": ".join(item.values()))


class DataStream:
    """"""
    def __init__(self):
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors = self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    continue
                continue
            print(f"DataStream error - Can't process element in stream: {element}")
  
    def print_processors_stats(self) -> None:
        pass



def test_numeric(instance: NumericProcessor) -> None:
    """Exercise validation, error handling, and FIFO extraction."""
    print("Testing Numeric Processor...")

    print(f" Trying to validate input '42': {instance.validate(42)}")

    print(f" Trying to validate input 'Hello': {instance.validate('Hello')}")

    # Deliberately skip validate() before ingest() so the guard
    # clause inside ingest() raises instead of silently corrupting
    # the storage with bad data.
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        instance.ingest("foo")
    except TypeError as e:
        print(f" Got exception: {e}")

    num_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_data}")
    instance.validate(num_data)
    instance.ingest(num_data)

    # output() always returns the oldest remaining item first, so
    # ranks come back in ascending order: 0, 1, 2.
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = instance.output()
        print(f" Numeric value {rank}: {value}")


def test_text(instance: TextProcessor) -> None:
    """Exercise validation and ingestion of a list of strings."""
    print("Testing Text Processor...")

    print(f" Trying to validate input '42': {instance.validate(42)}")

    txt_data = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {txt_data}")
    instance.validate(txt_data)
    instance.ingest(txt_data)

    print(" Extracting 1 value...")
    rank, value = instance.output()
    print(f" Text value {rank}: {value}")


def test_log(instance: LogProcessor) -> None:
    """Exercise validation and ingestion of a list of log entries."""
    print("Testing Log Processor...")

    print(f" Trying to validate input 'Hello': {instance.validate('Hello')}")

    log_data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f" Processing data: {log_data}")
    instance.validate(log_data)
    instance.ingest(log_data)

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = instance.output()
        print(f" Log entry {rank}: {value}")


def main() -> None:
    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    print("=== Code Nexus - Data Processor ===\n")
    test_numeric(num)

    print()
    test_text(txt)

    print()
    test_log(log)


if __name__ == "__main__":
    main()
