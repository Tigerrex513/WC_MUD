import random

class CommandHandler:
    def __init__(self, game_state, zone_manager):
        self.game_state = game_state
        self.zone_manager = zone_manager

    def update_on_tick(self):
        # Perform any necessary updates here
        pass

    def handle_command(self, command, args):
        if command == "quit":
            return self.quit()
        elif command == "help":
            return self.display_help()
        elif command == "explore":
            return self.explore()
        elif command == "move":
            return self.move(args)
        elif command == "look":
            return self.look(args)
        elif command == "inventory":
            return self.inventory()
        elif command == "take":
            return self.take(args)
        elif command == "drop":
            return self.drop(args)
        elif command == "equip":
            return self.equip(args)
        elif command == "remove":
            return self.remove(args)
        elif command == "say":
            return self.say(args)
        elif command == "shout":
            return self.shout(args)
        elif command == "attack":
            return self.attack()
        elif command == "use":
            return self.use(args)
        elif command == "score":
            return self.score()
        elif command == "save":
            return self.save()
        else:
            return "Unknown command. Type 'help' for a list of commands."

    def quit(self):
        self.game_state.player.save()
        return "quit"

    def display_help(self):
        return """
Available commands:
explore - Explore the current zone
move - Move to a different direction
look - Examine your surroundings
inventory - Check your inventory
take [item] - Pick up an item
drop [item] - Drop an item
equip [item] - Equip an item
remove [item] - Remove an equipped item
say [message] - Say something
shout [message] - Shout a message
attack - Initiate combat with an enemy
use [item] - Use an item
score - Check your character stats
save - Save your character
quit - Save and exit the game
"""

    def explore(self):
        current_zone = self.game_state.current_zone
        result = f"You explore {current_zone.name}. {current_zone.description}"
        
        if hasattr(current_zone, 'features'):
            result += f"\nFeatures: {', '.join(current_zone.features)}"
        
        if random.random() < 0.5:  # 50% chance of encounter
            encounter = random.choice(self.game_state.enemies)
            result += f"\nYou encounter a {encounter.name}!"
            self.game_state.current_enemy = encounter
        
        return result

    def move(self, args):
        if not args:
            return "Which direction do you want to go?"
        direction = args[0].lower()
        new_zone = self.zone_manager.move(self.game_state.current_zone.id, direction)
        if new_zone:
            self.game_state.change_zone(new_zone)
            return f"You moved to {new_zone.name}."
        else:
            return "You can't go that way."

    def look(self, args):
        if args:
            return self.game_state.player.look(args[0])
        else:
            return self.game_state.player.look()

    def inventory(self):
        return self.game_state.player.inventory_check()

    def take(self, args):
        if not args:
            return "What do you want to take?"
        return self.game_state.player.take(args[0])

    def drop(self, args):
        if not args:
            return "What do you want to drop?"
        return self.game_state.player.drop(args[0])

    def equip(self, args):
        if not args:
            return "What do you want to equip?"
        return self.game_state.player.equip(args[0])

    def remove(self, args):
        if not args:
            return "What do you want to remove?"
        return self.game_state.player.remove(args[0])

    def say(self, args):
        if not args:
            return "What do you want to say?"
        return self.game_state.player.say(" ".join(args))

    def shout(self, args):
        if not args:
            return "What do you want to shout?"
        return self.game_state.player.shout(" ".join(args))

    def attack(self):
        if not self.game_state.current_enemy:
            self.game_state.current_enemy = random.choice(self.game_state.enemies)
        return self.game_state.player.fight(self.game_state.current_enemy)

    def use(self, args):
        if not args:
            return "What do you want to use?"
        return self.game_state.player.use(args[0])

    def score(self):
        return self.game_state.player.score()

    def save(self):
        self.game_state.save_state()
        self.game_state.player.save()
        return "Game state and character saved successfully!"