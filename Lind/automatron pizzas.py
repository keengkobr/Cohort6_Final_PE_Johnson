import math

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

def equilateral_triangle_area(side_length):
    return (math.sqrt(3) / 4) * side_length ** 2

def square_area(side_length):
    return side_length ** 2

circle_total_area = 2 * circle_area(15)
circle_dough = 20
circle_efficiency = circle_total_area / circle_dough

triangle_area = equilateral_triangle_area(20)
triangle_dough = 20
triangle_efficiency = triangle_area / triangle_dough

square_area_value = square_area(18)
square_dough = 18
square_efficiency = square_area_value / square_dough

print("Automatron 1 (Circle) Efficiency:", round(circle_efficiency, 2))
print("Automatron 2 (Triangle) Efficiency:", round(triangle_efficiency, 2))
print("Automatron 3 (Square) Efficiency:", round(square_efficiency, 2))

efficiencies = {
    "Automatron 1 (Circle)": circle_efficiency,
    "Automatron 2 (Triangle)": triangle_efficiency,
    "Automatron 3 (square)": square_efficiency
}

best_automatron = max(efficiencies, key=efficiencies.get)
print("\n Most Efficient Automatron:", best_automatron)