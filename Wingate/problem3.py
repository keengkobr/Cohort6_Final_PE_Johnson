with open('input.txt', 'r') as file:
    mass_list = list(map(int, file))

    total_fuel = 0
    
    for num in mass_list:
        fuel_per_mod = num // 3 - 2
        total_fuel += fuel_per_mod
    
    print(total_fuel)
