Creating a complete fleet-tracker program in Python involves several components, including tracking vehicles, managing their data, visualizing their locations on a map, and possibly a user interface for interacting with the system. Below is a simplified version of such a program that focuses on tracking and basic management. This version will primarily log vehicle positions using random data (for demonstration) and include a basic command-line interface to interact with the program:

```python
import random
import time
from datetime import datetime
import threading

# Sample vehicle class
class Vehicle:
    def __init__(self, vehicle_id, latitude, longitude):
        self.vehicle_id = vehicle_id
        self.latitude = latitude
        self.longitude = longitude
        self.tracking_data = []

    def update_position(self, new_latitude, new_longitude):
        self.latitude = new_latitude
        self.longitude = new_longitude
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.tracking_data.append((self.latitude, self.longitude, timestamp))
        print(f"[INFO] Vehicle {self.vehicle_id} updated position to ({self.latitude}, {self.longitude}) at {timestamp}")

    def get_position(self):
        return self.latitude, self.longitude

    def get_tracking_data(self):
        return self.tracking_data

# Fleet management class
class Fleet:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle_id, latitude=0.0, longitude=0.0):
        if vehicle_id not in self.vehicles:
            self.vehicles[vehicle_id] = Vehicle(vehicle_id, latitude, longitude)
            print(f"[INFO] Vehicle {vehicle_id} added to fleet.")
        else:
            print(f"[WARNING] Vehicle {vehicle_id} already exists in fleet.")

    def update_vehicle_position(self, vehicle_id, latitude, longitude):
        try:
            vehicle = self.vehicles[vehicle_id]
            vehicle.update_position(latitude, longitude)
        except KeyError:
            print(f"[ERROR] Vehicle {vehicle_id} not found.")

    def get_vehicle_position(self, vehicle_id):
        try:
            vehicle = self.vehicles[vehicle_id]
            return vehicle.get_position()
        except KeyError:
            print(f"[ERROR] Vehicle {vehicle_id} not found.")
            return None

    def simulate_movement(self, vehicle_id, duration=10):
        try:
            vehicle = self.vehicles[vehicle_id]
            for _ in range(duration):
                # Simulate random movement
                new_latitude = vehicle.latitude + random.uniform(-0.01, 0.01)
                new_longitude = vehicle.longitude + random.uniform(-0.01, 0.01)
                vehicle.update_position(new_latitude, new_longitude)
                time.sleep(1)
        except KeyError:
            print(f"[ERROR] Vehicle {vehicle_id} not found.")

def main():
    fleet = Fleet()

    while True:
        print("\n[COMMANDS] add - add vehicle, update - update position, simulate - simulate movement, quit - exit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            vehicle_id = input("Enter vehicle ID: ").strip()
            try:
                latitude = float(input("Enter starting latitude: ").strip())
                longitude = float(input("Enter starting longitude: ").strip())
                fleet.add_vehicle(vehicle_id, latitude, longitude)
            except ValueError:
                print("[ERROR] Invalid latitude or longitude value.")

        elif command == "update":
            vehicle_id = input("Enter vehicle ID: ").strip()
            try:
                latitude = float(input("Enter new latitude: ").strip())
                longitude = float(input("Enter new longitude: ").strip())
                fleet.update_vehicle_position(vehicle_id, latitude, longitude)
            except ValueError:
                print("[ERROR] Invalid latitude or longitude value.")

        elif command == "simulate":
            vehicle_id = input("Enter vehicle ID: ").strip()
            try:
                duration = int(input("Enter simulation duration (seconds): ").strip())
                threading.Thread(target=fleet.simulate_movement, args=(vehicle_id, duration)).start()
            except ValueError:
                print("[ERROR] Invalid duration value.")

        elif command == "quit":
            print("Exiting Fleet Tracker.")
            break

        else:
            print("[ERROR] Unknown command.")

if __name__ == "__main__":
    main()
```

### Key Features of This Program:
- **Vehicle Class**: Models a vehicle with ID, latitude, and longitude.
- **Fleet Management**: Handles multiple vehicles, allowing you to add vehicles, update their positions, and simulate movement.
- **Error Handling**: Uses try-except blocks to catch and report exceptions such as invalid input or missing vehicles.
- **Simulation**: Includes a simplistic simulation of vehicle movement by updating position randomly over time.
- **Command-Line Interface**: Provides interactive commands to add vehicles, update positions, simulate movements, or exit the program.

### Instructions to Run:
1. Save the program in a Python file (e.g., `fleet_tracker.py`).
2. Run the program using a Python interpreter (`python fleet_tracker.py`).
3. Use the command prompts to interact with the fleet management system.

For a full-fledged implementation, consider integrating APIs for real-time data like GPS hardware or mapping services through libraries like `geopy` and visualization tools like `folium` or other mapping libraries.