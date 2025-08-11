# Evaluate which of the 3 robots produces more pizza per unit of dough
# robot1 uses 20 units of dough to produce 2 pizzas at 15 inch diameter
# robot2 uses 20 units of dough to produce 1 pizza at  20 inch side length in an equilater triangle
# robot3 uses 18 units of dough to produce 1 pizza at 18 inch side length in a square
import math

def pizza_efficiency():
    robot1 = round(2 * (math.pi * (15 / 2) ** 2), 2)  # Area of two pizzas with diameter 15 inches
    robot2 = round(18 ** 2 * (math.sqrt(3) / 4), 2)  # Area of equilateral triangle pizza with side length 20 inches
    robot3 = round(18 ** 2, 2)  # Area of square pizza with side length 18 inches

    print("Robot 1 produces", robot1, "square inches of pizza.")
    print("Robot 2 produces", robot2, "square inches of pizza.")
    print("Robot 3 produces", robot3, "square inches of pizza.")

    if robot1 > robot2 and robot1 > robot3:
        print("Robot 1 is the most efficient.")
    elif robot2 > robot1 and robot2 > robot3:
        print("Robot 2 is the most efficient.")
    elif robot3 > robot1 and robot3 > robot2:
        print("Robot 3 is the most efficient.")


pizza_efficiency()