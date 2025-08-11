import math


def pizza_deal_calculator(dough_per_area_pizza1, dough_per_area_pizza2, dough_per_area_pizza3):
    best_deal = dough_per_area_pizza1

    if best_deal > dough_per_area_pizza2:
        best_deal = dough_per_area_pizza2
    elif best_deal > dough_per_area_pizza3:
        best_deal = dough_per_area_pizza3

    print(f'The best deal is:  {best_deal}')

area_of_pizza1 = math.pi * (15 / 2) ** 2
total_pizza1_area = area_of_pizza1 * 2 
dough_per_area_pizza1 = 20 / total_pizza1_area
print(f'pizza 1 dough/area: {dough_per_area_pizza1}')

area_of_pizza2 = (( 3 * .5) / 4) * 18 ** 2
dough_per_area_pizza2 = 20 / area_of_pizza2
print(f'pizza 2 dough/area: {dough_per_area_pizza2}')


area_of_pizza3 = 18 ** 2
dough_per_area_pizza3 = 18 / area_of_pizza3
print(f'pizza 3 dough/area: {dough_per_area_pizza3}')



pizza_deal_calculator(dough_per_area_pizza1, dough_per_area_pizza2, dough_per_area_pizza3)


