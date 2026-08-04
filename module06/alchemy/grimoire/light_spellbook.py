from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    allowed = ["earth", "air", "fire", "water"]
    return allowed


def light_spell_record(spell_name: str, ingredients: str) -> str:
    ret = validate_ingredients(ingredients)
    if ret.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({ret})"
    return f"Spell rejected: {spell_name} ({ret})"
