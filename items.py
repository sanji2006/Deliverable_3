from dice import Dice


class Weapon:
    """A weapon uses a Dice object to determine its damage (Task 3)."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        # Composition: the weapon delegates the roll to its dice object.
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        return f"Weapon(name={self.name!r}, damage_dice={self.damage_dice!r})"
