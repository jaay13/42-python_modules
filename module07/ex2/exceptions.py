class InvalidStrategyError(Exception):
    def __init__(self, creature_name: str, strategy_name: str):
        self.error_message = (
            f"Invalid Creature '{creature_name}' "
            f"for this {strategy_name} strategy"
        )
        super().__init__(self.error_message)
