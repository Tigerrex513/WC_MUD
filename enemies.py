class Enemy:
    def __init__(self, name, health, damage, description):
        self.name = name
        self.health = health
        self.damage = damage
        self.description = description

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")
        target.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"The {self.name} took {amount} damage!")
        if self.health <= 0:
            self.death()

    def death(self):
        print(f"The {self.name} dies due to taking too much damage!")

    def __str__(self):
        return f"{self.name} - HP: {self.health}, Damage: {self.damage}\n{self.description}"


class Badger(Enemy):
    def __init__(self):
        super().__init__(
            name="Badger",
            health=70,
            damage=40,
            description="A large, aggressive animal with powerful claws and teeth."
        )


class Fox(Enemy):
    def __init__(self):
        super().__init__(
            name="Fox",
            health=30,
            damage=8,
            description="A cunning and agile predator known for its quick attacks."
        )


class Twoleg(Enemy):
    def __init__(self):
        super().__init__(
            name="Twoleg",
            health=100,
            damage=5,
            description="A towering human with strange tools and unpredictable behavior."
        )


class Eagle(Enemy):
    def __init__(self):
        super().__init__(
            name="Eagle",
            health=25,
            damage=12,
            description="A majestic bird of prey with sharp talons and a powerful beak."
        )


class Hawk(Enemy):
    def __init__(self):
        super().__init__(
            name="Hawk",
            health=20,
            damage=10,
            description="A swift and deadly bird of prey with keen eyesight."
        )


# Sample enemies list for easy access
def get_sample_enemies():
    return [Badger(), Fox(), Twoleg(), Eagle, Hawk()]


if __name__ == "__main__":
    # Test the enemies
    enemies = get_sample_enemies()
    for enemy in enemies:
        print(enemy)

