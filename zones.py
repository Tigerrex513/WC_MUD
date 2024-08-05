import csv
from typing import Dict, List, Optional

class Zone:
    def __init__(self, id: int, name: str, type: str, description: str, x_coord: int, y_coord: int,
                 enemies: List[str], scenarios: List[str], features: List[str], exits: Dict[str, int]):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.enemies = enemies
        self.scenarios = scenarios
        self.features = features
        self.exits = exits

class ZoneManager:
    def __init__(self, filename: str = 'zones.csv'):
        self.filename = filename
        self.zones: Dict[int, Zone] = {}
        self.load_zones()

    def load_zones(self):
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                exits = {}
                if row['exits']:  # Check if exits is not empty
                    for exit in row['exits'].split('|'):
                        parts = exit.split(':')
                        if len(parts) == 2:
                            exits[parts[0]] = int(parts[1])
                zone = Zone(
                    id=int(row['id']),
                    name=row['name'],
                    type=row['type'],
                    description=row['description'],
                    x_coord=int(row['x_coord']),
                    y_coord=int(row['y_coord']),
                    enemies=row['enemies'].split('|') if row['enemies'] else [],
                    scenarios=row['scenarios'].split('|') if row['scenarios'] else [],
                    features=row['features'].split('|') if row['features'] else [],
                    exits=exits
                )
                self.zones[zone.id] = zone

    def get_zone_by_id(self, zone_id: int) -> Optional[Zone]:
        return self.zones.get(zone_id)

    def get_zone_by_coordinates(self, x_coord: int, y_coord: int) -> Optional[Zone]:
        for zone in self.zones.values():
            if zone.x_coord == x_coord and zone.y_coord == y_coord:
                return zone
        return None

    def move(self, current_zone_id: int, direction: str) -> Optional[Zone]:
        current_zone = self.get_zone_by_id(current_zone_id)
        if current_zone and direction in current_zone.exits:
            return self.get_zone_by_id(current_zone.exits[direction])
        return None

    def save_zones(self):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'name', 'type', 'description', 'x_coord', 'y_coord', 'enemies', 'scenarios', 'features', 'exits'])
            writer.writeheader()
            for zone in self.zones.values():
                writer.writerow({
                    'id': zone.id,
                    'name': zone.name,
                    'type': zone.type,
                    'description': zone.description,
                    'x_coord': zone.x_coord,
                    'y_coord': zone.y_coord,
                    'enemies': '|'.join(zone.enemies),
                    'scenarios': '|'.join(zone.scenarios),
                    'features': '|'.join(zone.features),
                    'exits': '|'.join([f"{k}:{v}" for k, v in zone.exits.items()])
                })

    @property
    def all_zones(self) -> List[Zone]:
        return list(self.zones.values())