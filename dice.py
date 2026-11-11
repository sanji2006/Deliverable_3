import random

class Dice:
    """An n-sided dice."""

    def __init__(self, sides: int = 6) -> None:
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a number from 1 to sides."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Allow d20() as a shortcut for d20.roll()."""
        return self.roll()
