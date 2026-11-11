from character import Character


class Battle:
    """Manage turn-based combat between two characters (Task 5)."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        if hero is enemy:
            raise ValueError("A battle requires two different characters.")
        self.hero = hero
        self.enemy = enemy
        self.round_number = 0

    def play_round(self) -> None:
        # Dead characters cannot start a round or retaliate.
        if not (self.hero.is_alive and self.enemy.is_alive):
            return
        self.round_number += 1
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
        print(f"Round {self.round_number}: {self.hero.name} {self.hero.hp} HP | "
              f"{self.enemy.name} {self.enemy.hp} HP")

    def simulate_battle(self, max_rounds: int = 1000) -> Character | None:
        # A limit also handles setups where armor blocks every possible attack.
        if max_rounds < 1:
            raise ValueError("max_rounds must be positive.")
        rounds_played = 0
        while self.hero.is_alive and self.enemy.is_alive:
            if rounds_played >= max_rounds:
                print("Draw: round limit reached.")
                return None
            self.play_round()
            rounds_played += 1
        if not self.hero.is_alive and not self.enemy.is_alive:
            print("Draw: both characters have zero HP.")
            return None
        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"Winner: {winner.name} with {winner.hp} HP!")
        return winner
