"""
This program flies through a drone course... Digitally.
"""
from Drone_Course_Simulator import Drone #Import drone
drone = Drone("Task 1", (1300, 700), 270) #Create drone object

drone.up(5) #Move drone up 5 Meters
drone.forward(200) #Move drone forward 200 Meters
drone.curve(0, 225, 50, -325, 850, 60) #Curve drone
drone.launch() #Launch drone