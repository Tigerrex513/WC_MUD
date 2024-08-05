import time
import random
from character import character_creator
from enemies import EnemyManager, get_sample_enemies
from zones import ZoneManager
from command_handler import CommandHandler
from game_state import GameState

TICK_DURATION = 6  # seconds

def get_time_passage_message():
    messages = [
        "Time passes...",
        "The world around you continues to move.",
        "You sense the passage of time.",
        "The sun inches across the sky.",
        "A gentle breeze reminds you that time is flowing.",
        "The shadows shift slightly.",
    ]
    return random.choice(messages)

def main():
    print("\nWelcome to the Warrior Cats MUD!")
    
    player = character_creator()
    enemy_manager = EnemyManager('enemies.csv')
    enemies = get_sample_enemies(enemy_manager)
    zone_manager = ZoneManager('zones.csv')
    zones = zone_manager.zones  # Assuming ZoneManager has a zones attribute

    try:
        game_state = GameState.load_state(player, zones, enemies)
        print("Game state loaded successfully.")
    except FileNotFoundError:
        starting_zone = zone_manager.get_zone_by_id(1)
        game_state = GameState(player, starting_zone, enemies)
        print("New game state created.")

    command_handler = CommandHandler(game_state, zone_manager)
    
    last_tick_time = time.time()
    last_time_message = time.time()
    MESSAGE_INTERVAL = 15  # Show a time passage message every minute

    while True:
        current_time = time.time()
        
        if current_time - last_tick_time >= TICK_DURATION:
            game_state.update_time()
            command_handler.update_on_tick()
            last_tick_time = current_time

            if current_time - last_time_message >= MESSAGE_INTERVAL:
                print(f"\n{get_time_passage_message()}\n")
                last_time_message = current_time

        print(f"\nYou are in {game_state.current_zone.name}. {game_state.current_zone.description}")
        print("What do you want to do?")
        print("Type 'help' for a list of commands.\n")
        
        user_input = input("> ").lower().split()
        command = user_input[0] if user_input else ""
        args = user_input[1:] if len(user_input) > 1 else []
        
        result = command_handler.handle_command(command, args)
        
        if result == "quit":
            print("\nSaving game state before quitting...")
            game_state.save_state()
            player.save()
            print("Goodbye!")
            break
        else:
            print(result)

if __name__ == "__main__":
    main()