from character import character_creator, Character
from enemies import EnemyManager, get_sample_enemies
import random

def display_menu():
    print("\nWhat do you want to do?")
    print("1. Explore current zone")
    print("2. Move to a different zone")
    print("3. Describe character")
    print("4. Save character")
    print("5. Fight an enemy")
    print("6. Quit")

def main():
    print("Welcome to the Warrior Cats MUD!")
    
    # Create or load player character
    player = character_creator()
    
    # Initialize EnemyManager and load enemies
    enemy_manager = EnemyManager('enemies.csv')
    enemies = get_sample_enemies(enemy_manager)
    
    while True:
        display_menu()
        action = input("> ").lower()
        
        if action == "6" or action == "quit":
            print("Saving character before quitting...")
            player.save()
            print("Goodbye!")
            break
        
        elif action == "1" or action == "explore":
            player.explore_current_zone()
            
            # Chance to encounter an enemy
            if random.random() < 0.5:  # 50% chance of encounter
                encounter = random.choice(enemies)
                print(f"\nYou encounter a {encounter.name}!")
                
                while encounter.health > 0 and player.health > 0:
                    print("\nWhat do you want to do?")
                    print("1. Fight")
                    print("2. Run")
                    print("3. Hide")
                    player_action = input("> ").lower()
                    
                    if player_action == "1" or player_action == "fight":
                        player.fight(encounter)
                    elif player_action == "2" or player_action == "run":
                        if player.run():
                            break
                    elif player_action == "3" or player_action == "hide":
                        if player.hide():
                            break
                    else:
                        print("Unknown action. Try again.")
                    
                    if encounter.health > 0:
                        encounter.attack(player)
        
        elif action == "2" or action == "move":
            player.get_current_zone_info()
            direction = input("Which direction do you want to go? ").lower()
            player.move(direction)
        
        elif action == "3" or action == "describe":
            print(player.describe())
        
        elif action == "4" or action == "save":
            player.save()
            print("Character saved successfully!")
        
        elif action == "5" or action == "fight":
            encounter = random.choice(enemies)
            print(f"\nYou encounter a {encounter.name}!")
            
            while encounter.health > 0 and player.health > 0:
                print("\nWhat do you want to do?")
                print("1. Fight")
                print("2. Run")
                print("3. Hide")
                player_action = input("> ").lower()
                
                if player_action == "1" or player_action == "fight":
                    player.fight(encounter)
                elif player_action == "2" or player_action == "run":
                    if player.run():
                        break
                elif player_action == "3" or player_action == "hide":
                    if player.hide():
                        break
                else:
                    print("Unknown action. Try again.")
                
                if encounter.health > 0:
                    encounter.attack(player)
        
        else:
            print("Unknown action. Try again.")

if __name__ == "__main__":
    main()