from character import character_creator
from enemies import get_sample_enemies, Enemy
import random

'''
TO DO LIST: 
1) fix bug where you can't continue fighting the enemy after a failed run/hide 
2) make it say "You cannot explore" when you encounter an enemy and try to explore
3) when running the enemies file, the eagle information is missing

'''

def main():
    print("Welcome to the Warrior Cats MUD!")
    
    # Create player character
    player = character_creator()
    
    # Load sample enemies
    enemies = get_sample_enemies()
    
    while True:
        print("\nWhat do you want to do?")
        action = input("> ").lower()
        
        if action == "quit":
            print("Goodbye!")
            break
        elif action == "explore":
            print("You venture into the unknown...")
            encounter = random.choice(enemies)
            print(f"You encounter a {encounter.name}!")
            
            while encounter.health > 0 and player.health > 0:
                print("\nWhat do you want to do?")
                player_action = input("> ").lower()
                
                if player_action == "fight":
                    player.fight(encounter)
                elif player_action == "run":
                    player.run()
                    break
                elif player_action == "hide":
                    player.hide()
                    break
                else:
                    print("Unknown action. Try again.")
                    
                if encounter.health > 0:
                    encounter.attack(player)
                    
        else:
            print("Unknown action. Try again.")

if __name__ == "__main__":
    main()
