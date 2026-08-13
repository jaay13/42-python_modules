"""Master's Tower: decorators that wrap and enhance any spell.

Every decorator uses functools.wraps so the wrapped function keeps
its own name and docstring.
"""

import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    """Time a spell and report how long it took.

    Prints "Casting <name>..." before and
    "Spell completed in X.XXX seconds" after, then returns the
    original result.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        ret = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Spell completed in {elapsed:.3f} seconds")

        return ret

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Build a decorator that rejects spells below min_power.

    A valid power runs the function normally; otherwise the wrapper
    returns "Insufficient power for this spell".
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Build a decorator that retries a spell that raises.

    Prints "Spell failed, retrying... (attempt n/max_attempts)" per
    retry and returns "Spell casting failed after <n> attempts" if
    every attempt fails.
    """
    raise NotImplementedError


class MageGuild:
    """A guild whose members cast validated spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """True if name is 3+ characters of letters and spaces only."""
        raise NotImplementedError

    # Decorate with @power_validator(min_power=10) once it exists.
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell, returning what happened.

        On success: "Successfully cast <spell_name> with <power>
        power".
        """
        raise NotImplementedError


def main() -> None:
    """Demonstrate each decorator and the guild's static method."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
