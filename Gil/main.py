#!/usr/bin/env python3

import math
import pandas as pd

def telemetryChallenge():
    distanceUnits = input("\nDistance units [\"miles\" | \"km\"]: ")

    if distanceUnits == "miles":
        distanceMiles = int(input("Miles above Mars: "))
        
        # 1 mile = 1760 yards
        #        = 5280 feet
        #        = 63360
        
        yards = distanceMiles * 1760
        feet = yards * 3
        inches = feet * 12

        print(f"\nFor {distanceMiles} miles:")
        print(f"    Yards: {yards}, Feet: {feet}, Inches: {inches}")
        
    elif distanceUnits == "km":
        distanceKM = int(input("KM above Mars"))

        print(f"{distanceKM * 1000},{distanceKM * 1000000}, {distanceKM * 1000000000}")

def calcAreaCircle(diameter):
    # Find circle area
    areaCircle = math.pi * ((diameter / 2) ** 2)
    autoCircleArea = areaCircle * 2
    
    return autoCircleArea

def calcAreaTriangle(side):
    # Find triangle area
    autoEquiTriangleArea = ((3 ** 0.5) / 4) * (side ** 2)

    return autoEquiTriangleArea

def calcAreaSquare(side):
    # Find square area
    autoSquareArea = side ** 2

    return autoSquareArea
    
def resourceChallenge():
    print(f"\nPizza Circle (area / dough): {calcAreaCircle(15) / 20:.2f}")
    print(f"Pizza Triangle (area / dough): {calcAreaTriangle(20) / 20:.2f}")
    print(f"Pizza Square (area / dough): {calcAreaSquare(18) / 18:.2f}")

def fuelChallenge():
    with open("input.txt", "r") as file:
        masses = file.read().splitlines()
    
    mass = 0
    for m in masses:
        mass += round(int(m) / 3) - 2
    
    print(f"\nTotal Mass: {mass}")
    
def main():
    medalists = pd.read_csv("all_olympic_medalists.csv")

    print(medalists.medal[medalists["country"] == "United States"].value_counts)

    telemetryChallenge()

    resourceChallenge()

    fuelChallenge()
    
if __name__ == "__main__":
    main()