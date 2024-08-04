from enemies import Enemy

class Scenario:
    def __init__(self, zone):
        self.zone = zone

    def trigger(self, player):
        print(f"You encounter a scenario in {self.zone}")
        enemy = Enemy("Goblin", 10, 2)
        print(f"A wild {enemy.name} appears!")
        while enemy.health > 0 and player.health > 0:
            action = input("Fight or Run? ")
            if action.lower() == "fight":
                enemy.health -= player.strength
                print(f"You hit the {enemy.name} for {player.strength} damage!")
                if enemy.health <= 0:
                    print(f"You defeated the {enemy.name}!")
                    break
                enemy.attack(player)
            elif action.lower() == "run":
                print("You ran away!")
                break
            else:
                print("Invalid action!")
