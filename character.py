# Object-oriented game simulator
# Based on lecture 8 by Turid Torheim, NMBU, 2026
from __future__ import annotations


class Character:
    """Represents a character in the RPG."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character.

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100).
            damage (int): Damage dealt when the character attacks (default = 10).
        """
        self.name = name
        self.hp_max = hp_max
        self._hp = hp_max  # Protected attribute: only the character changes it
        self.damage = damage

    def take_damage(self, amount: int) -> None:
        """Reduce this character's own HP. HP never goes below 0."""
        if amount < 0:
            raise ValueError("Damage cannot be negative.")
        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """Increase this character's own HP. HP never goes above hp_max."""
        if amount < 0:
            raise ValueError("Healing cannot be negative.")
        self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target: Character) -> None:
        """Attack the target by asking it to take damage."""
        target.take_damage(self.damage)

    def introduce(self) -> None:
        """Print a string that introduces the character."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of the character object."""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of the character object."""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property: True if the character has more than 0 HP."""
        return self._hp > 0