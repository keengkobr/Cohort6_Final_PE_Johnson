import math

def calculate_fuel(mass):
    divided = mass // 3
    fuel = divided - 2
    return max(fuel, 0), divided

def total_fuel_required(filename):
    fuel_values = []
    with open(filename, 'r') as file:
        for line in file:
            mass = int(line)
            fuel, divided = calculate_fuel(mass)
            fuel_values.append(fuel)
            print(F"Mass: {mass} -> {mass} // 3 = {divided} -> {divided} - 2 = {fuel}")
    
    total = sum(fuel_values)
    print("\n Total Fuel Required:", total)
    return total
    

filename = 'inputs.txt'
total_fuel = total_fuel_required(filename)
