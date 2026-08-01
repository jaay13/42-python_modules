from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Common interface for every data processor of the Code Nexus."""

    def __init__(self) -> None:
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
        return self._storage.pop(0)

    def _store(self, item: str) -> None:
        """Append one processed item and give it the next rank."""
        self._storage.append((self._rank, item))
        self._rank += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(item)


class LogProcessor(DataProcessor):
    def _is_log(self, data: Any) -> bool:
        return isinstance(data, dict) and all(
            isinstance(k, str) and isinstance(v, str) for k, v in data.items()
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self._is_log(item) for item in data)
        return self._is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(": ".join(item.values()))


def test_numeric(instance: NumericProcessor) -> None:
    print("Testing Numeric Processor...")

    print(f" Trying to validate input '42': {instance.validate(42)}")

    print(f" Trying to validate input 'Hello': {instance.validate('Hello')}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        instance.ingest("foo")
    except TypeError as e:
        print(f" Got exception: {e}")

    num_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_data}")
    instance.validate(num_data)
    instance.ingest(num_data)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = instance.output()
        print(f" Numeric value {rank}: {value}")


def test_text(instance: TextProcessor) -> None:
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
