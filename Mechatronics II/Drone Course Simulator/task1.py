"""
This program flies through a drone course... Digitally.
"""
from Drone_Course_Simulator import Drone #Import drone
drone = Drone("Task 1", (1300, 700), 270) #Create drone object

drone.up(5) #Move drone up 5 Meters
drone.forward(250) #Move drone forward 250 Meters
drone.rotate_ccw(20) #Rotate drone counter-clockwise 20 Degrees
drone.forward(150) #Move drone forward 100 Meters
drone.rotate_ccw(30) #Rotate drone counter-clockwise 30 Degrees
drone.forward(210) #Move drone forward 100 Meters
drone.rotate_ccw(40) #Rotate drone counter-clockwise 90 Degrees
drone.forward(800) #Move drone forward 800 Meters
drone.rotate_ccw(90) #Rotate drone counter-clockwise 90 Degrees
drone.forward(150) #Move drone forward 150 Meters
drone.up(3) #Move drone up 3 Meters
drone.forward(100) #Move drone forward 100 Meters
drone.down(2) #Move drone down 2 Meters
drone.forward(100) #Move drone forward 100 Meters
drone.down(2) #Move drone down 2 Meters
drone.forward(225) #Move drone forward 250 Meters
drone.rotate_ccw(90) #Rotate drone counter-clockwise 90 Degrees
drone.forward(235) #Move drone forward 300 Meters
drone.rotate_ccw(90) #Rotate drone counter-clockwise 90 Degrees
drone.forward(110) #Move drone forward 100 Meters
drone.rotate_cw(90) #Rotate drone clockwise 90 Degrees
drone.forward(400) #Move drone forward 200 Meters
drone.rotate_cw(90) #Rotate drone counter-clockwise 90 Degrees
drone.forward(110) #Move drone forward 100 Meters
drone.rotate_ccw(90) #Rotate drone counter-clockwise 90 Degrees
drone.forward(300) #Move drone forward 100 Meters

drone.launch() #Launch drone