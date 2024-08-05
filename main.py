from character import character_creator, Character
from enemies import EnemyManager, get_sample_enemies
import random

def display_help():
    print("\nAvailable commands:")
    print("explore - Explore the current zone")
    print("move - Move to a different direction")
    print("look - Examine your surroundings")
    print("inventory - Check your inventory")
    print("take [item] - Pick up an item")
    print("drop [item] - Drop an item")
    print("equip [item] - Equip an item")
    print("remove [item] - Remove an equipped item")
    print("say [message] - Say something")
    print("shout [message] - Shout a message")
    print("attack - Initiate combat with an enemy")
    print("use [item] - Use an item")
    print("score - Check your character stats")
    print("save - Save your character")
    print("quit - Save and exit the game")

def main():
    print("/n/nWelcome to the Warrior Cats MUD!/n/n")
    
    # Create or load player character
    player = character_creator()
    
    # Initialize EnemyManager and load enemies
    enemy_manager = EnemyManager('enemies.csv')
    enemies = get_sample_enemies(enemy_manager)
    
    while True:
        print("\nWhat do you want to do?")
        print("You can [look], [move], [explore] or type [help] for more options.")
        print("Type 'help' for a list of commands.")
        action = input("> ").lower().split()
        
        command = action[0] if action else ""
        args = action[1:] if len(action) > 1 else []
        
        if command == "quit":
            print("/nSaving character before quitting...")
            player.save()
            print("/n/nGoodbye!")
            break
        
        elif command == "help":
            display_help()
        
        elif command == "explore":
            player.explore_current_zone()
            
            # Chance to encounter an enemy
            if random.random() < 0.5:  # 50% chance of encounter
                encounter = random.choice(enemies)
                print(f"\nYou encounter a {encounter.name}!")
                
                while encounter.health > 0 and player.health > 0:
                    print("\nWhat do you want to do?")
                    print("You can [fight], [run], or [hide].")
                    player_action = input("> ").lower()
                    
                    if player_action == "fight":
                        player.fight(encounter)
                    elif player_action == "run":
                        if player.run():
                            break
                    elif player_action == "hide":
                        if player.hide():
                            break
                    else:
                        print("Unknown action. Try again.")
                    
                    if encounter.health > 0:
                        encounter.attack(player)
        
        elif command == "move":
            player.get_current_zone_info()
            direction = input("Which direction do you want to go? ").lower()
            player.move(direction)
        
        elif command == "look":
            if args:
                player.look(args[0])
            else:
                player.look()
        
        elif command == "inventory":
            player.inventory_check()
        
        elif command == "take":
            if args:
                player.take(args[0])
            else:
                print("What do you want to take?")
        
        elif command == "drop":
            if args:
                player.drop(args[0])
            else:
                print("What do you want to drop?")
        
        elif command == "equip":
            if args:
                player.equip(args[0])
            else:
                print("What do you want to equip?")
        
        elif command == "remove":
            if args:
                player.remove(args[0])
            else:
                print("What do you want to remove?")
        
        elif command == "say":
            if args:
                player.say(" ".join(args))
            else:
                print("What do you want to say?")
        
        elif command == "shout":
            if args:
                player.shout(" ".join(args))
            else:
                print("What do you want to shout?")
        
        elif command == "attack":
            encounter = random.choice(enemies)
            print(f"\nYou encounter a {encounter.name}!")
            player.fight(encounter)
        
        elif command == "use":
            if args:
                player.use(args[0])
            else:
                print("What do you want to use?")
        
        elif command == "score":
            player.score()
        
        elif command == "save":
            player.save()
            print("Character saved successfully!")
        
        else:
            print("Unknown action. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()