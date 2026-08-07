class InvalidStrategyError(Exception):
    """Raised when a BattleStrategy is used on an unsuitable Creature."""

    def __init__(self, creature_name: str, strategy_label: str):
        self.error_message = (
            f"Invalid Creature '{creature_name}' "
            f"for this {strategy_label} strategy"
        )
        super().__init__(self.error_message)
