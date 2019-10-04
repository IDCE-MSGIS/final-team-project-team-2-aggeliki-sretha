# Name: Aggeliki Barberopoulou and Surendra Shrestha
# Assignment title: Final Project
# Time to complete: 1 hour.
# Created: October 4th 2019
# Modified: October 5th, 2019
# Description: This script calculates rain runoff for a watershed based on the user input value of precipitation

#Terms
# P = precipitation (inches/day)
# ET = evapotranspiration (inches/day)
# R = Runoff depth (inches/day)
# L = Length of the watershed (meters)
# B = Breadth of the watershed (meters)
# A = Area of the field (meters squared)

def calculate_runoff(P):
    ET = 0.6*P  # Evapotranspiration (ET) in inches per day
    R = P - ET # Runoff (R) in inches per day
    return R

P = input('Enter a value for precipitation: ') # User input value of precipitation in inches per day
Runoff = calculate_runoff(P) # Assign variable to the output of runoff function

# Convert inches to meters
Runoff_meter = Runoff * 0.0254 # Converting runoff from inches to meters per day
print "The runoff depth in meters per day: ", Runoff_meter


### Calculate Area of the field
def calculate_area(L, B): #Both length and breadth are in meters
    A = L * B
    return A
    
L = input('Enter a value for length of field: ') # User input value of length in meters
B = input('Enter a value for breadth of field: ') # User input value of breadth in meters
Area = calculate_area(L, B) # Assign variable to the output of function
print "The area of the watershed in meter squared : ", Area

#Calculate Streamflow
Streamflow = Runoff_meter * Area # Calculating streamflow in cubic meter per day
print "The streamflow in cubic meters per day: ", Streamflow


