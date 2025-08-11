# Read input.txt file containing the mass of modules
# Create a formula to find the fuel needed, take its mass, divide by 3, round down, subtract 2
# Calculate the total fuel for each module
# Add all the fuel values together
import math

def calculate_fuel():
    total_fuel = 0
    with open('Day 12/input.txt', 'r') as file:
        for line in file:
            mass = int(line.strip())
            fuel = math.floor((mass // 3) - 2) # Calculate fuel needed for the module
            total_fuel += fuel
    print("Total fuel required:", total_fuel)

calculate_fuel()