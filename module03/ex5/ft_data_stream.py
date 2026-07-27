import random
from typing import Generator

PLAYERS = ["jason", "van", "benjx", "nathi", "timmy"]

ACTIONS = ["run", "sleep", "jump", "move", "fly", "swim"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Yield an endless stream of random (player, action) events."""

    # yield suspends the loop, so it only runs when a value is requested
    while True:
        random_player = random.choice(PLAYERS)
        random_action = random.choice(ACTIONS)
        yield random_player, random_action


def consume_event(
    event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    """Yield events picked at random, removing each one from event_list."""

    # Stop once the caller's list has been drained
    while len(event_list) > 0:
        # pop() removes the element at the index and hands it back
        yield event_list.pop(random.randrange(len(event_list)))


def main() -> None:
    print("=== Game Data Stream Processor ===")

    # Create the generator once, then pull values from that same object
    events = gen_event()

    # 1000 random events from gen_event
    for i in range(1000):
        event = next(events)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    # Ten more events from the very same stream, put into a list
    event_list = []
    for i in range(10):
        event_list.append(next(events))
    print(f"\nBuilt list of 10 events: {event_list}")

    # The generator drives the loop and stops itself when the list is
    # empty, so no counter is needed. It pops from event_list directly,
    # which is why the list visibly shrinks between iterations.
    for event_remove in consume_event(event_list):
        print(f"\nGot event from list: {event_remove}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
