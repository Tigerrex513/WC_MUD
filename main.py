import time
import random
import queue
import threading
from character import character_creator
from enemies import EnemyManager, get_sample_enemies
from zones import ZoneManager
from command_handler import CommandHandler
from game_state import GameState

TICK_DURATION = 6  # seconds
MESSAGE_INTERVAL = 30  # Show a time passage message every 30 seconds

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

def input_with_timeout(timeout):
    import select
    import sys

    input_queue = queue.Queue()

    def get_input():
        input_queue.put(sys.stdin.read(1))

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    start_time = time.time()
    while time.time() - start_time < timeout:
        if not input_queue.empty():
            return input_queue.get()
        time.sleep(0.1)

    return None

def main():
    print("\nWelcome to the Warrior Cats MUD!")
    
    player = character_creator()
    enemy_manager = EnemyManager('enemies.csv')
    enemies = get_sample_enemies(enemy_manager)
    zone_manager = ZoneManager('zones.csv')
    
    try:
        game_state = GameState.load_state(player, zone_manager.all_zones, enemies)
        print("Game state loaded successfully.")
    except FileNotFoundError:
        starting_zone = zone_manager.get_zone_by_id(1)
        if starting_zone is None:
            raise ValueError("Starting zone (id: 1) not found in zones.csv")
        game_state = GameState(player, starting_zone, enemies)
        print("New game state created.")

    command_handler = CommandHandler(game_state, zone_manager)
    
    last_tick_time = time.time()
    last_time_message = time.time()
    user_input = ""

    print(f"\nYou are in {game_state.current_zone.name}. {game_state.current_zone.description}")
    print("\nWhat do you want to do? Use [help] for a list of commands.")

    while True:
        current_time = time.time()
        
        if current_time - last_tick_time >= TICK_DURATION:
            game_state.update_time()
            command_handler.update_on_tick()
            last_tick_time = current_time

            if current_time - last_time_message >= MESSAGE_INTERVAL:
                print(f"\n{get_time_passage_message()}")
                last_time_message = current_time

        # Non-blocking input check
        if user_input == "":
            user_input = input_with_timeout(TICK_DURATION)

        # Process complete commands
        if user_input is not None and user_input.strip() != "":
            command_parts = user_input.lower().split()
            command = command_parts[0] if command_parts else ""
            args = command_parts[1:] if len(command_parts) > 1 else []
            
            result = command_handler.handle_command(command, args)
            
            if result == "quit":
                print("\nSaving game state before quitting...")
                game_state.save_state()
                player.save()
                print("Goodbye!")
                break
            else:
                print(result)
            
            print(f"\nYou are in {game_state.current_zone.name}. {game_state.current_zone.description}")
            print("\nWhat do you want to do?")
            print("Type 'help' for a list of commands.")
            
            user_input = ""  # Reset input buffer

if __name__ == "__main__":
    main()
