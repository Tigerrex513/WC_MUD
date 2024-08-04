import csv
from typing import Dict, List, Tuple

class Zone:
    def __init__(self, id: int, name: str, type: str, description: str, coordinates: Tuple[int, int],
                 enemies: List[str], scenarios: List[str], features: List[str], exits: Dict[str, int]):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.coordinates = coordinates
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
                zone = Zone(
                    id=int(row['id']),
                    name=row['name'],
                    type=row['type'],
                    description=row['description'],
                    coordinates=tuple(map(int, row['coordinates'].split(','))),
                    enemies=row['enemies'].split('|'),
                    scenarios=row['scenarios'].split('|'),
                    features=row['features'].split('|'),
                    exits={k: int(v) for k, v in [exit.split(':') for exit in row['exits'].split('|')]}
                )
                self.zones[zone.id] = zone

    def get_zone_by_id(self, zone_id: int) -> Zone:
        return self.zones.get(zone_id)

    def get_zone_by_coordinates(self, coordinates: Tuple[int, int]) -> Zone:
        for zone in self.zones.values():
            if zone.coordinates == coordinates:
                return zone
        return None

    def move(self, current_zone_id: int, direction: str) -> Zone:
        current_zone = self.get_zone_by_id(current_zone_id)
        if direction in current_zone.exits:
            return self.get_zone_by_id(current_zone.exits[direction])
        return None

    def save_zones(self):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'name', 'type', 'description', 'coordinates', 'enemies', 'scenarios', 'features', 'exits'])
            writer.writeheader()
            for zone in self.zones.values():
                writer.writerow({
                    'id': zone.id,
                    'name': zone.name,
                    'type': zone.type,
                    'description': zone.description,
                    'coordinates': f"{zone.coordinates[0]},{zone.coordinates[1]}",
                    'enemies': '|'.join(zone.enemies),
                    'scenarios': '|'.join(zone.scenarios),
                    'features': '|'.join(zone.features),
                    'exits': '|'.join([f"{k}:{v}" for k, v in zone.exits.items()])
                })