import csv

class GameState:
    def __init__(self, player, current_zone, enemies):
        self.player = player
        self.current_zone = current_zone
        self.enemies = enemies
        self.current_enemy = None
        self.global_time = 0
        self.weather = "clear"

    def update_time(self):
        self.global_time += 1
        # You can add time-based events here

    def change_zone(self, new_zone):
        self.current_zone = new_zone

    def save_state(self, filename='game_state.csv'):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['global_time', 'weather', 'current_zone_id'])
            writer.writerow([self.global_time, self.weather, self.current_zone.id])

    @classmethod
    def load_state(cls, player, zones, enemies, filename='game_state.csv'):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            data = next(reader)
            global_time, weather, current_zone_id = int(data[0]), data[1], int(data[2])
        
        current_zone = next(zone for zone in zones if zone.id == current_zone_id)
        game_state = cls(player, current_zone, enemies)
        game_state.global_time = global_time
        game_state.weather = weather
        return game_state