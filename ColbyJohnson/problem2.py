import math

def compute_area(shape, size, count=1):
    if shape == "circle":
        radius = size / 2
        area = math.pi * radius ** 2
    elif shape == "triangle":
        area = (math.sqrt(3) / 4) * size ** 2
    elif shape == "square":
        area = size ** 2
    return count * area

automatons = {
    "Automatron 1": {"shape": "circle", "size": 15, "count": 2, "dough": 20},
    "Automatron 2": {"shape": "triangle", "size": 20, "count": 1, "dough": 20},
    "Automatron 3": {"shape": "square", "size": 18, "count": 1, "dough": 18}
}

best_deal = None
best_value = 0

for name, data in automatons.items():
    area = compute_area(data["shape"], data["size"], data["count"])
    value = area / data["dough"]
    print(f"{name}: Area = {area:.2f}, Value = {value:.2f} per dough unit")
    if value > best_value:
        best_value = value
        best_deal = name

print(f"\nBest deal: {best_deal}")