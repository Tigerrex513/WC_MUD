

'''
CatDoes = input(f"{name} happens upon a fox den. Will {name} attack? ")
if CatDoes == "yes":
    print("You fight valiantly, but the fox is too strong for you.")
elif CatDoes == "no":
    print("You run to camp, and a patrol is gathered to chase it off the territory.")
else:
    print("The fox attacks, but you are able to run away.")
'''

import random

# List of scenarios
scenarios = [
    "You happen upon a fox den.",
    "You encounter a babbling brook with rushing water.",
    "An eagle is swooping overhead."
]

def character_creator():
    print("Welcome to the Warrior Cats character creator!")
    
    # Get character details from the user
    name = input("What is your character called? > ")
    gender = input("What is your character's gender? > ")
    strengths = input("What are your character's strengths? > ")
    weaknesses = input("What are your character's weaknesses? > ")
    
    # Print character details
    print("\nCharacter Summary:")
    print(f"Name: {name}")
    print(f"Gender: {gender}")
    print(f"Strengths: {strengths}")
    print(f"Weaknesses: {weaknesses}")
    
    print(f"\n{name} says, 'Thanks for creating me!'")
    
    return name, gender, strengths, weaknesses

def character_fight(name, target):
    if target == "":
        target == "the enemy"
    print(f"{name} decides to fight {target}.")

def what_do_you_want_to_do(scenario, name):
    print(f"\n{scenario}")
    action = input(f"{name}, what do you want to do? > ")
    
    # You might want to process the action or store it for later use
    print(f"{name} decides to {action}.")
    
    
def main():
    # Create a character
    name, gender, strengths, weaknesses = character_creator()
    
    # Choose a random scenario
    scenario = random.choice(scenarios)
    
    # Present the scenario and get user action
    what_do_you_want_to_do(scenario, name)

# Run the main function
if __name__ == "__main__":
    main()
