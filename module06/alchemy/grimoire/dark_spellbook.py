from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    allowed = ["bats", "frogs", "arsenic", "eyeball"]
    return allowed


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    ret = validate_ingredients(ingredients)
    if ret.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({ret})"
    return f"Spell rejected: {spell_name} ({ret})"
