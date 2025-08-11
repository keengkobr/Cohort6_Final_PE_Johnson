import math

def fuel_req(mass):
    fuel = (math.floor(mass / 3)) - 2
    return fuel

def calc_total():
    total_fuel = 0
    with open('C:\\Users\\Dylan Temple\\Documents\\Classwork\\Project One\\input.txt', 'r') as file:
        for line in file:
            mass = int(line.strip())
            total_fuel += fuel_req(mass)
    print(f"Total fuel needed: {total_fuel}")

calc_total()