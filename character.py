import os
import csv
from zones import ZoneManager

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
        self.inventory = []
        self.equipped_items = {}

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return f"{self.name} has been defeated."
        else:
            return f"{self.name} has {self.health} health remaining."

    def heal(self, amount):
        self.health = min(100, self.health + amount)
        return f"{self.name} has been healed. Current health: {self.health}"

    def add_to_inventory(self, item):
        self.inventory.append(item)
        return f"{item} has been added to your inventory."

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return f"{item} has been removed from your inventory."
        return f"You don't have {item} in your inventory."

    def equip_item(self, item):
        if item in self.inventory:
            self.equipped_items[item] = True
            return f"You equip {item}."
        return f"You don't have {item} in your inventory."

    def unequip_item(self, item):
        if item in self.equipped_items:
            del self.equipped_items[item]
            return f"You unequip {item}."
        return f"You don't have {item} equipped."

    def get_stats(self):
        return f"""
Character Stats for {self.name}:
Strength: {self.strength}
Agility: {self.agility}
Knowledge: {self.knowledge}
Health: {self.health}
"""

    def save(self):
        if not os.path.exists('characters'):
            os.makedirs('characters')
        
        filename = f"characters/{self.name.lower()}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['attribute', 'value'])
            for attr, value in self.__dict__.items():
                if attr != 'zone_manager':  # We don't want to save the ZoneManager instance
                    writer.writerow([attr, value])
        return f"Character {self.name} saved to {filename}"

    @classmethod
    def load(cls, name):
        filename = f"characters/{name.lower()}.csv"
        if not os.path.exists(filename):
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
        
        return character

    def __str__(self):
        return f"{self.name} - Str: {self.strength}, Agi: {self.agility}, Kno: {self.knowledge}, HP: {self.health}"

def character_creator():
    choice = input("Do you want to create a new character or load an existing one? (new/load): ").lower()
    
    if choice == 'load':
        name = input("Enter the name of the character to load: ").lower()
        character = Character.load(name)
        if character is None:
            print("Failed to load character. Creating a new one instead.")
            return character_creator()
        return character
    
    name = input("What is your character called? > ")
    gender = input("What is your character's gender? > ")
    strengths = input("What are your character's strengths? > ")
    weaknesses = input("What are your character's weaknesses? > ")
    
    strength = int(input("Strength (1-10): "))
    agility = int(input("Agility (1-10): "))
    knowledge = int(input("Knowledge (1-10): "))
    
    character = Character(name, gender, strengths, weaknesses, strength, agility, knowledge)
    
    print("\nCharacter Summary:")
    print(str(character))
    print(f"Gender: {character.gender}")
    print(f"Strengths: {character.strengths}")
    print(f"Weaknesses: {character.weaknesses}")
    
    print(f"\n{name} says, 'Thanks for creating me!'")
    
    character.save()
    print(f"Character {name} has been saved.")
    
    return character

if __name__ == "__main__":
    player = character_creator()
    print(player.get_stats())