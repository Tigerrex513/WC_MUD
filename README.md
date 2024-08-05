# WC_MUD

## Description
This is a MUD (Multi-User Dungeon) based on the popular "Warrior Cats" series! Players can create a character and navigate through various zones, encountering enemies and scenarios. The game features a robust character system, dynamic zone navigation, and an expandable enemy framework.

## Project Structure

The project is structured into several modules to handle different aspects of the game:

- **main.py**: The main script that initializes the game, manages the main loop, and handles user inputs. It integrates all other modules to create the game experience.

- **character.py**: Handles character creation, stats, actions, and persistence. It includes the `Character` class with methods for movement, combat, inventory management, and more.

- **enemies.py**: Defines enemy behaviors and stats. It uses a CSV-based system for easy addition and modification of enemies.

- **zones.py**: Defines different areas in the game world. It includes a `Zone` class and a `ZoneManager` class for handling zone navigation and properties.

- **scenarios.py**: Defines various scenarios players can encounter (to be implemented).

- **utils.py**: Contains helper functions used across different modules (to be implemented).

## Technical Details

### Character System
- Characters are instances of the `Character` class.
- Character attributes include name, gender, strengths, weaknesses, and stats (strength, agility, knowledge, health).
- Characters can perform various actions like move, fight, hide, use items, etc.
- Character data is persisted using CSV files, allowing for save/load functionality.

### Zone System
- Zones are managed by the `ZoneManager` class.
- Each zone is an instance of the `Zone` class with properties like ID, name, type, description, coordinates, enemies, scenarios, features, and exits.
- Zones are defined in a `zones.csv` file for easy editing and expansion.
- The zone system uses an X-Y coordinate system for spatial representation.

### Enemy System
- Enemies are defined in an `enemies.csv` file.
- The `EnemyManager` class handles loading and managing enemy data.
- Enemies have properties like name, health, damage, and description.

### Game Loop
- The main game loop in `main.py` handles user input and game state.
- It integrates character actions, zone navigation, and enemy encounters.

## Getting Started

To get started with WC_MUD, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Tigerrex513/WC_MUD.git
    cd WC_MUD
    ```

2. **Ensure you have the required CSV files**:
   - `zones.csv`: Defines all game zones.
   - `enemies.csv`: Defines all possible enemies.

3. **Run the game**:
    ```bash
    python main.py
    ```

## Character Creation and Loading

When you start the game, you'll be prompted to create a new character or load an existing one. Character data is stored in CSV files in a `characters` directory.

## Zones

The game world is divided into different zones, each represented by a unique ID and coordinates. Players can move between zones using cardinal directions (north, south, east, west).

## Enemies

Enemies are dynamically loaded from the `enemies.csv` file. Each enemy has properties like health, damage, and a description. Encounters with enemies are managed in the main game loop.

## Future Improvements

- Implement the scenarios system for more dynamic gameplay.
- Expand the inventory and item usage system.
- Develop a more comprehensive combat system.
- Implement a quest or mission system.

---

Enjoy your journey in the Warrior Cats universe and may StarClan guide your path!