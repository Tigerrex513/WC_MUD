import random
import os
import csv
from zone_manager import ZoneManager

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
        self.current_zone_id = 1
        self.zone_manager = ZoneManager('zones.csv')

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

    def explore_current_zone(self):
        current_zone = self.zone_manager.get_zone_by_id(self.current_zone_id)
        print(f"Exploring {current_zone.name}...")
        print(current_zone.description)
        print("Features:", ", ".join(current_zone.features))
        print("Possible enemies:", ", ".join(current_zone.enemies))
        print("Possible scenarios:", ", ".join(current_zone.scenarios))

    def move(self, direction):
        new_zone = self.zone_manager.move(self.current_zone_id, direction)
        if new_zone:
            self.current_zone_id = new_zone.id
            print(f"You have moved to {new_zone.name}.")
            self.explore_current_zone()
        else:
            print("You can't go that way.")

    def get_current_zone_info(self):
        current_zone = self.zone_manager.get_zone_by_id(self.current_zone_id)
        print(f"You are currently in {current_zone.name}.")
        print("Possible exits:", ", ".join(current_zone.exits.keys()))

    def describe(self):
        """Provide a detailed description of the character."""
        current_zone = self.zone_manager.get_zone_by_id(self.current_zone_id)
        description = f"""
Character Description for {self.name}:
----------------------------------------
Gender: {self.gender}
Health: {self.health}/100

Statistics:
- Strength: {self.strength}/10
- Agility: {self.agility}/10
- Knowledge: {self.knowledge}/10

Strengths: {self.strengths}
Weaknesses: {self.weaknesses}

Current Location: {current_zone.name}
Zone Type: {current_zone.type}

Character Status:
{self.name} is a {self.gender} cat with {self.health} health points. 
They excel in {self.strengths}, but struggle with {self.weaknesses}.
Currently, they are in {current_zone.name}, a {current_zone.type} zone.

Nearby threats may include: {', '.join(current_zone.enemies)}
Potential scenarios: {', '.join(current_zone.scenarios)}

Notable features in the area:
{', '.join(current_zone.features)}

Available exits: {', '.join(current_zone.exits.keys())}
        """
        return description

    def save(self):
        """Save the character's attributes to a CSV file."""
        if not os.path.exists('assets'):
            os.makedirs('assets')
        
        filename = f"assets/{self.name}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['attribute', 'value'])
            for attr, value in self.__dict__.items():
                if attr != 'zone_manager':  # We don't want to save the ZoneManager instance
                    writer.writerow([attr, value])
        print(f"Character {self.name} saved to {filename}")

    @classmethod
    def load(cls, name):
        """Load a character from a CSV file."""
        filename = f"assets/{name}.csv"
        if not os.path.exists(filename):
            print(f"No saved character found with name {name}")
            return None

        attributes = {}
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                attr, value = row
                attributes[attr] = value

        # Convert numeric strings back to integers
        for attr in ['strength', 'agility', 'knowledge', 'health', 'current_zone_id']:
            if attr in attributes:
                attributes[attr] = int(attributes[attr])

        character = cls(
            name=attributes['name'],
            gender=attributes['gender'],
            strengths=attributes['strengths'],
            weaknesses=attributes['weaknesses'],
            strength=attributes['strength'],
            agility=attributes['agility'],
            knowledge=attributes['knowledge'],
            health=attributes['health']
        )
        character.current_zone_id = attributes['current_zone_id']

        print(f"Character {name} loaded from {filename}")
        return character

    def __str__(self):
        return f"{self.name} - Str: {self.strength}, Agi: {self.agility}, Kno: {self.knowledge}, HP: {self.health}"

def character_creator():
    print("Welcome to the Warrior Cats character creator!")
    
    # Ask if the user wants to create a new character or load an existing one
    choice = input("Do you want to create a new character or load an existing one? (new/load): ").lower()
    
    if choice == 'load':
        name = input("Enter the name of the character to load: ")
        character = Character.load(name)
        if character is None:
            print("Failed to load character. Creating a new one instead.")
            return character_creator()
        return character
    
    # If not loading, create a new character
    name = input("What is your character called? > ")
    gender = input("What is your character's gender? > ")
    strengths = input("What are your character's strengths? > ")
    weaknesses = input("What are your character's weaknesses? > ")
    
    # Assign stats
    strength = int(input("Strength (1-10): "))
    agility = int(input("Agility (1-10): "))
    knowledge = int(input("Knowledge (1-10): "))
    
    # Create the character
    character = Character(name, gender, strengths, weaknesses, strength, agility, knowledge)
    
    # Print character details
    print("\nCharacter Summary:")
    print(str(character))
    print(f"Gender: {character.gender}")
    print(f"Strengths: {character.strengths}")
    print(f"Weaknesses: {character.weaknesses}")
    
    print(f"\n{name} says, 'Thanks for creating me!'")
    
    # Save the character
    character.save()
    
    return character

if __name__ == "__main__":
    player = character_creator()
    print(player.describe())