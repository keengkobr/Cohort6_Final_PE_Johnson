
def miles_above():
    num_miles = input("Enter the number of miles:")
    miles_float = 0
    try:
        miles_float = float(num_miles)
    except:
        print("You need to input a numeric value!")
        miles_above()
    yards = miles_float * 1760
    feet = yards * 3
    inches = feet * 12
    print(f"Yards: {yards}\nFeet: {feet}\nInches: {inches}")    


def km_above():
    num_km = input("Enter the number of kilometers:")
    km_float = 0
    try:
        km_float = float(num_km)
    except:
        print("You need to input a numeric value!")
        km_above()
    meters = km_float * 1000
    centimeters = meters * 100
    milimeters = centimeters * 10
    print(f"Meters: {meters}\nCentimeters: {centimeters}\nMilimeters: {milimeters}")  

def get_UI():
    user_pmt = input("Miles above Mars or Kilometers above Mars?")
    if user_pmt == "Miles above Mars":
        miles_above()
    elif user_pmt == "Kilometers above Mars":
        km_above()
    else:
        print("Invalid Answer!")
        get_UI()

get_UI()