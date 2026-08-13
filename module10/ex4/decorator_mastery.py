"""Master's Tower: decorators that wrap and enhance any spell.

Every decorator uses functools.wraps so the wrapped function keeps
its own name and docstring.
"""

import inspect
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
            bound = inspect.signature(func).bind(*args, **kwargs)
            power = bound.arguments["power"]
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
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """A guild whose members cast validated spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """True if name is 3+ characters of letters and spaces only."""
        return (
            all(c.isalpha() or c == " " for c in name) and len(name) >= 3
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell, returning what happened.

        On success: "Successfully cast <spell_name> with <power>
        power".
        """
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Demonstrate each decorator and the guild's static method."""

    print("Testing spell timer...")

    @spell_timer
    def jump_boost() -> str:
        time.sleep(0.21)
        return "You now have jump boost II for 5 min!"

    print(f"Result: {jump_boost()}")

    print("\nTesting retrying spell")

    @retry_spell(3)
    def failing() -> str:
        raise RuntimeError("fizzled")

    print(failing())

    @retry_spell(3)
    def succeeding() -> str:
        return "You now have speed II for 3 min!"

    print(succeeding())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Jason"))
    print(MageGuild.validate_mage_name("J4s0n"))
    guild = MageGuild()
    valid = guild.cast_spell("Lightning", 15)
    invalid = guild.cast_spell("Lightning", 8)
    print(valid)
    print(invalid)


if __name__ == "__main__":
    main()
