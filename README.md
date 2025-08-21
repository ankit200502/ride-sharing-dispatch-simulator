Ride-Sharing Dispatch Simulator
This project is a command-line simulator for a ride-sharing service's dispatch system. It demonstrates how to efficiently match riders with the most suitable drivers based on real-world factors like location and driver ratings.

Features
Driver & Rider Management: The simulator handles the creation and management of driver and rider profiles, each with unique attributes like location and rating.

Intelligent Matching: It uses a priority queue to assign the "best" available driver to a ride request. The matching algorithm considers both proximity to the rider and the driver's rating to determine the optimal match.

Queue-based Requests: Incoming ride requests are managed in a standard queue to ensure they are processed in the order they were received.

Ride History: A comprehensive history of all completed rides is maintained, recording key details like the rider and driver IDs, trip distance, and timestamp.

Scalable Architecture: The use of efficient data structures like deque (for the request queue) and heapq (for the driver priority queue) makes the system scalable and capable of handling multiple requests and drivers simultaneously.

How to Run
Save the Code: Save the provided Python code into a file named dispatch_simulator.py.

Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the script using the following command:

Bash

python dispatch_simulator.py
View Output: The script will automatically simulate the process of adding drivers, requesting a ride, and dispatching a driver. The results of the simulation will be printed directly to the console. You can easily modify the if __name__ == "__main__": block to add more drivers, riders, and requests to test the system further.

Sample Output
The following output demonstrates the simulator's logic, from requesting a ride to the final dispatch and history record.

Ride requested by rider R1
Dispatching driver D1 to rider R1

--- Ride History ---
Rider: R1, Driver: D1, Distance: 1.41
