class Player:

    def __init__(self, name: str, health):
        self.name = name
        self._health = health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health < 0 or new_health > 100:
            print("\nInvalid Health! Should Be Between 0 To 100")
        else:
            print(f"\nHealth Before: {self._health}")
            self._health = new_health
            print(f"Current Health: {self._health}")

    def take_damage(self, damage):
        self.health -= damage
        print(f"\nDamage = {damage}")
        print(f"Health After Taking Damage = {self.health}")

    def heal(self, amount):
        self.health += amount
        print(f"\nHealing = {amount}")
        print(f"Health After Healing = {self.health}")


p1 = Player("Hardik", 100)

print(f"Player Health is {p1.health}\n")

p1.health = 90

p1.take_damage(30)
p1.heal(20)