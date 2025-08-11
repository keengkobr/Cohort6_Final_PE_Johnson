 #Write a program to ask the user if they want to input miles or kilometers above Mars
# If miles, display number of yards, feet, and inches in that many miles
# If km, display meters, centimeters, and millimeters in that many kilometers

m_or_km = input("Enter 'm' for miles or 'km' for kilometers: ")

def distance():
    if m_or_km == "m":
        miles = float(input("Enter the number of miles: "))
        yards = miles * 1760
        feet = miles * 5280
        inches = miles * 63360
        print(f"{miles} miles is equal to {yards} yards, {feet} feet, and {inches} inches.")
    elif m_or_km == "km":
        kilometers = float(input("Enter the number of kilometers: "))
        meters = kilometers * 1000
        centimeters = kilometers * 100000
        millimeters = kilometers * 1000000
        print(f"{kilometers} kilometers is equal to {meters} meters, {centimeters} centimeters, and {millimeters} millimeters.")
    else:
        print("Congrats, you are going to die unless you figure out this basic problem. Please enter 'miles' or 'kilometers'.")
        distance()

distance()