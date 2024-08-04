import csv
from typing import List, Dict

class Enemy:
    def __init__(self, name: str, health: int, damage: int, description: str):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.description = description

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")
        target.take_damage(self.damage)

    def take_damage(self, amount: int):
        self.health -= amount
        print(f"The {self.name} took {amount} damage!")
        if self.health <= 0:
            self.death()

    def death(self):
        print(f"The {self.name} dies due to taking too much damage!")

    def __str__(self):
        return f"{self.name} - HP: {self.health}/{self.max_health}, Damage: {self.damage}\n{self.description}"

class EnemyManager:
    def __init__(self, csv_file: str):
        self.enemies: Dict[str, Enemy] = {}
        self.load_enemies(csv_file)

    def load_enemies(self, csv_file: str):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                enemy = Enemy(
                    name=row['name'],
                    health=int(row['health']),
                    damage=int(row['damage']),
                    description=row['description']
                )
                self.enemies[row['name']] = enemy

    def get_enemy(self, name: str) -> Enemy:
        return self.enemies.get(name)

    def get_all_enemies(self) -> List[Enemy]:
        return list(self.enemies.values())

def get_sample_enemies(enemy_manager: EnemyManager) -> List[Enemy]:
    return [
        enemy_manager.get_enemy("Badger"),
        enemy_manager.get_enemy("Fox"),
        enemy_manager.get_enemy("Twoleg"),
        enemy_manager.get_enemy("Eagle"),
        enemy_manager.get_enemy("Hawk")
    ]

if __name__ == "__main__":
    # Test the enemies
    enemy_manager = EnemyManager('enemies.csv')
    enemies = get_sample_enemies(enemy_manager)
    for enemy in enemies:
        print(enemy)