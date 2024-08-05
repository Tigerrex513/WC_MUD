import random

class CommandHandler:
    def __init__(self, game_state, zone_manager):
        self.game_state = game_state
        self.zone_manager = zone_manager

    def update_on_tick(self):
        # Perform any necessary updates here
        pass

    def handle_command(self, command, args):
        commands = {
            "quit": self.quit,
            "help": self.display_help,
            "explore": self.explore,
            "move": self.move,
            "look": self.look,
            "inventory": self.inventory,
            "take": self.take,
            "drop": self.drop,
            "equip": self.equip,
            "remove": self.remove,
            "say": self.say,
            "shout": self.shout,
            "attack": self.attack,
            "use": self.use,
            "score": self.score,
            "save": self.save
        }
        
        if command in commands:
            return commands[command](args) if args else commands[command]()
        else:
            return "Unknown command. Type 'help' for a list of commands."

    def quit(self):
        self.game_state.player.save()
        return "quit"

    def display_help(self):
        return """
Available commands:
explore - Explore the current zone
move [direction] - Move to a different direction
look [target] - Examine your surroundings or a specific target
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
        current_zone = self.game_state.current_zone
        if args:
            target = args[0]
            # Implement logic to describe the target
            return f"You examine the {target}."
        else:
            return f"You are in {current_zone.name}. {current_zone.description}"

    def inventory(self):
        player = self.game_state.player
        if player.inventory:
            return "Your inventory contains: " + ", ".join(player.inventory)
        else:
            return "Your inventory is empty."

    def take(self, args):
        if not args:
            return "What do you want to take?"
        item = args[0]
        # Implement logic to check if item is in the current zone and can be picked up
        return self.game_state.player.add_to_inventory(item)

    def drop(self, args):
        if not args:
            return "What do you want to drop?"
        item = args[0]
        return self.game_state.player.remove_from_inventory(item)

    def equip(self, args):
        if not args:
            return "What do you want to equip?"
        item = args[0]
        return self.game_state.player.equip_item(item)

    def remove(self, args):
        if not args:
            return "What do you want to remove?"
        item = args[0]
        return self.game_state.player.unequip_item(item)

    def say(self, args):
        if not args:
            return "What do you want to say?"
        message = " ".join(args)
        return f"{self.game_state.player.name} says: {message}"

    def shout(self, args):
        if not args:
            return "What do you want to shout?"
        message = " ".join(args)
        return f"{self.game_state.player.name} shouts: {message}"

    def attack(self):
        if not self.game_state.current_enemy:
            self.game_state.current_enemy = random.choice(self.game_state.enemies)
        enemy = self.game_state.current_enemy
        player = self.game_state.player
        result = f"{player.name} attacks the {enemy.name}!\n"
        result += enemy.take_damage(player.strength)
        if enemy.health > 0:
            result += f"\n{enemy.name} counterattacks!\n"
            result += player.take_damage(enemy.damage)
        else:
            result += f"\n{enemy.name} has been defeated!"
            self.game_state.current_enemy = None
        return result

    def use(self, args):
        if not args:
            return "What do you want to use?"
        item = args[0]
        # Implement item usage logic
        return f"You use the {item}."

    def score(self):
        return self.game_state.player.get_stats()

    def save(self):
        self.game_state.save_state()
        return self.game_state.player.save()