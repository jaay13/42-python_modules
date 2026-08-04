# from .elements import create_air
# is the 'relative' approach
# and would be the same as writing
# from alchemy.elements import create_air
# which is the 'absolute' approach
# in this example

from .elements import create_air
from .potions import healing_potion as heal
from .potions import strength_potion
from .transmutation import lead_to_gold

__all__ = ["create_air", "heal", "lead_to_gold", "strength_potion"]
