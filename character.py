import random

class Character:
    def __init__(self, name, gender, strengths, weaknesses, strength, agility, knowledge, health=100):
        self.name = name
        self.gender = gender
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.strength = strength
        self.agility = agility
        self.knowledge = knowledge
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated.")
        else:
            print(f"{self.name} has {self.health} health remaining.")

    def run(self):
        success = random.randint(0, 100) < (self.agility * 10)
        if success:
            print(f"{self.name} successfully ran away!")
        else:
            print(f"{self.name} failed to run away!")

    def fight(self, enemy):
        print(f"{self.name} attacks the {enemy.name}!")
        enemy.take_damage(self.strength)
        if enemy.health > 0:
            enemy.attack(self)

    def hide(self):
        success = random.randint(0, 100) < (self.agility * 10)
        if success:
            print(f"{self.name} successfully hid from danger!")
        else:
            print(f"{self.name} failed to hide!")

    @staticmethod
    def create_character():
        print("Create your character!")
        name = input("Name: ")
        strength = int(input("Strength (1-10): "))
        agility = int(input("Agility (1-10): "))
        knowledge = int(input("Knowledge (1-10): "))
        return Character(name, strength, agility, knowledge)

    def __str__(self):
        return f"{self.name} - Str: {self.strength}, Agi: {self.agility}, Kno: {self.knowledge}, HP: {self.health}"

def character_creator():
    print("Welcome to the Warrior Cats character creator!")
    
    # Get character details from the user
    name = input("What is your character called? > ")
    gender = input("What is your character's gender? > ")
    strengths = input("What are your character's strengths? > ")
    weaknesses = input("What are your character's weaknesses? > ")
    
    # Assign stats
    strength = int(input("Strength (1-10): "))
    agility = int(input("Agility (1-10): "))
    knowledge = int(input("Knowledge (1-10): "))
    
    # Print character details
    print("\nCharacter Summary:")
    print(f"Name: {name}")
    print(f"Gender: {gender}")
    print(f"Strengths: {strengths}")
    print(f"Weaknesses: {weaknesses}")
    print(f"Strength: {strength}")
    print(f"Agility: {agility}")
    print(f"Knowledge: {knowledge}")
    
    print(f"\n{name} says, 'Thanks for creating me!'")
    
    return Character(name, gender, strengths, weaknesses, strength, agility, knowledge)

# Sample character actions for testing
if __name__ == "__main__":
    player = character_creator()
    print(player)

    # Dummy enemy for testing
    class DummyEnemy:
        def __init__(self, name, health):
            self.name = name
            self.health = health
            self.damage = 5

        def take_damage(self, amount):
            self.health -= amount
            if self.health <= 0:
                print(f"{self.name} has been defeated.")
            else:
                print(f"{self.name} has {self.health} health remaining.")

        def attack(self, target):
            print(f"{self.name} attacks {target.name} for {self.damage} damage!")
            target.take_damage(self.damage)

    enemy = DummyEnemy("Test Enemy", 30)

    # Test actions
    player.fight(enemy)
    player.run()
    player.hide()
