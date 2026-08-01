"""Code Nexus - Data Stream.

Defines an abstract ``DataProcessor`` interface and three concrete
processors (numeric, text, log) that each know how to validate and
ingest their own kind of data, while sharing the same public API.
On top of that, ``DataStream`` holds a list of registered
``DataProcessor`` instances and routes each element of a mixed input
stream to whichever one accepts it.

How does polymorphism let ``DataStream`` handle different data types
without knowing their specific implementations? ``DataStream`` only
ever calls ``proc.validate(element)`` and ``proc.ingest(element)``
through the shared ``DataProcessor`` interface. It never inspects
``element``'s type itself, and it never checks which concrete
subclass ``proc`` is -- at runtime, Python dispatches each call to
whichever subclass the object actually is, so ``NumericProcessor``,
``TextProcessor``, and ``LogProcessor`` each apply their own
validation and storage rules without ``DataStream`` needing an
``isinstance`` chain or any other knowledge of their internals.

The benefit is decoupling: ``DataStream``'s routing logic is written
once against the abstract interface and never has to change when a
new kind of data shows up. Supporting it is just a matter of writing
a new ``DataProcessor`` subclass and registering an instance -- the
stream-processing code stays exactly the same. It also keeps each
processor's own logic isolated and independently testable, instead
of concentrating type-specific branching inside ``DataStream``.
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
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break 
            else:
                print(f"DataStream error - Can't process element in stream: {element}")
  
    def print_processors_stats(self) -> None:
        if len(self._processors) == 0:
            print("No processor found, no data")
        else:
            for proc in self._processors:
                print(
                    f"{type(proc).__name__.replace("Processor", " Processor")}: total {proc._rank} items processed, "
                    f"remaining {len(proc._storage)} on processor"
                )


def main() -> None:
    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    stream.register_processor(num)

    data = ['Hello World', [3.14, -1, 2.71], 
            [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]

    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(txt)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(data)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num.output()
    for _ in range(2):
        txt.output()
    log.output()

    print("== DataStream statistics ==")
    stream.print_processors_stats()
    


if __name__ == "__main__":
    main()
