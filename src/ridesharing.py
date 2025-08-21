import heapq
import uuid
import math
from collections import deque
from datetime import datetime

# A simple class to hold ride history
class RideHistory:
    def __init__(self, rider_id, driver_id, distance, timestamp):
        self.rider_id = rider_id
        self.driver_id = driver_id
        self.distance = distance
        self.timestamp = timestamp

# Driver and Rider classes
class Driver:
    def __init__(self, id, location, rating):
        self.id = id
        self.location = location
        self.rating = rating
        self.is_available = True

class Rider:
    def __init__(self, id, location, destination):
        self.id = id
        self.location = location
        self.destination = destination

class RideRequest:
    def __init__(self, rider, timestamp):
        self.rider = rider
        self.timestamp = timestamp

# Simulator core
class DispatchSimulator:
    def __init__(self):
        self.ride_requests = deque()
        self.available_drivers = []  # Priority Queue (min-heap)
        self.ride_history = []
        self.drivers = {} # For quick lookup

    def add_driver(self, driver):
        self.drivers[driver.id] = driver
        # Add driver to the priority queue with a high initial priority
        # A tuple (priority_value, driver_object) is used
        heapq.heappush(self.available_drivers, (0, driver.id))

    def request_ride(self, rider):
        request = RideRequest(rider, datetime.now())
        self.ride_requests.append(request)
        print(f"Ride requested by rider {rider.id}")

    def calculate_priority(self, rider_loc, driver_loc, driver_rating):
        distance = math.sqrt((rider_loc[0] - driver_loc[0])**2 + (rider_loc[1] - driver_loc[1])**2)
        # We want to minimize distance and maximize rating. 
        # So we subtract a scaled rating from the distance.
        # A lower value is a higher priority.
        return distance - (driver_rating * 1) # Rating weight can be adjusted

    def match_drivers_and_riders(self):
        if not self.ride_requests or not self.available_drivers:
            return

        # Get the next ride request
        request = self.ride_requests.popleft()
        
        # Re-evaluate priorities of all available drivers based on this request
        temp_heap = []
        while self.available_drivers:
            # Pop driver from heap
            priority, driver_id = heapq.heappop(self.available_drivers)
            driver = self.drivers[driver_id]
            # Calculate new priority and push to a temporary heap
            new_priority = self.calculate_priority(request.rider.location, driver.location, driver.rating)
            heapq.heappush(temp_heap, (new_priority, driver.id))
        
        # Restore the main heap with new priorities
        self.available_drivers = temp_heap

        # Get the best available driver
        priority, driver_id = heapq.heappop(self.available_drivers)
        best_driver = self.drivers[driver_id]
        
        # Assign the ride
        print(f"Dispatching driver {best_driver.id} to rider {request.rider.id}")
        
        # Record ride history
        ride_history_entry = RideHistory(request.rider.id, best_driver.id, priority + (best_driver.rating * 1), datetime.now())
        self.ride_history.append(ride_history_entry)
        best_driver.is_available = False # Set driver to unavailable

# Example Usage
if __name__ == "__main__":
    sim = DispatchSimulator()

    # Add some drivers
    drivers_data = [
        {"id": "D1", "loc": (1, 5), "rating": 4.8},
        {"id": "D2", "loc": (10, 2), "rating": 4.5},
        {"id": "D3", "loc": (5, 8), "rating": 4.9}
    ]
    for d in drivers_data:
        sim.add_driver(Driver(d["id"], d["loc"], d["rating"]))
    
    # Request a ride
    rider1 = Rider(id="R1", location=(2, 6), destination=(15, 20))
    sim.request_ride(rider1)
    
    # Run the dispatcher
    sim.match_drivers_and_riders()

    # Display results
    print("\n--- Ride History ---")
    for ride in sim.ride_history:
        print(f"Rider: {ride.rider_id}, Driver: {ride.driver_id}, Distance: {ride.distance:.2f}")
