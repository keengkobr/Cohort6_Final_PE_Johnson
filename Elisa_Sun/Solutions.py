import pandas as pd

df = pd.read_csv('Files/all_olympic_medalists.csv')

#pd.set_option('display.max_columns', None)

print("---------------------")
print(df[df['country'] == "United States"].count())


#####Problem 1 #########
user_input = input("Please choose Miles above Mars or Kilometers above Mars: ")

if user_input == "Miles above Mars":
    second_input = input("Please enter the number of miles: ")
    def yards(miles):
        return miles * 1760
    def feet(miles):
        return miles * 5280
    def inches(miles):
        return miles * 63360
    print(f"{second_input} miles in yards is", yards(int(second_input)))
    print(f"{second_input} miles in feet is", feet(int(second_input)))
    print(f"{second_input} miles in inches is", inches(int(second_input)))

elif user_input == "Kilometers above Mars":
    second_input = input("Please enter the number of kilometers: ")
    def yards(km):
        return km * 1093.6133
    def feet(km):
        return km * 3280.8399
    def inches(km):
        return km * 39370.0787
    print(f"{second_input} km in yards is", yards(int(second_input)))
    print(f"{second_input} km in feet is", feet(int(second_input)))
    print(f"{second_input} km in inches is", inches(int(second_input)))

#####Problem 2########

def pizza_area(radius):
    return 3.14159265358979323846 * (int(radius)/2) ** 2
# radius = input(f"Insert radius: ")
# print("Area is", pizza_area(f"{radius}"))
print("Pizza area is", pizza_area(15))

units = 20
first = units / (2*(pizza_area(15)))
print("Cost per square inch is", first)

import math
second_area = math.sqrt(500) * 10
print("Second pizza area is", {second_area})

units_2 = 20
second = units_2 / second_area
print("Cost per square inch is", second)

third_area = 18 ** 2
print("Third pizza area is", {third_area})

units_3 = 18
third = units_3 / third_area
print("Cost per square inch is", third)

##### Problem 3 #######
with open('Files/input.txt', 'r') as file:
    mass = file.readlines()

import math

new_list = []
for item in mass:
    new_item = item.strip("\n")
    number = math.floor(int(new_item) / 3) - 2
    new_list.append(number)
print(sum(new_list))
