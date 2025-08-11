def convert_miles(miles):
    yards = miles * 1760
    feet = miles * 5280
    inches = miles * 63360
    print(f"\nTelemetry Data (Miles Above Mars):")
    print(f"{miles} miles = {yards:.2f} yards")
    print(f"{miles} miles = {feet:.2f} feet")
    print(f"{miles} miles = {inches:.2f} inches")

def convert_kilometers(km):
    meters = km * 1000
    centimeters = km * 100000
    millimeters = km * 1_000_000
    print(f"\nTelemetry Data (Kilometers Above Mars):")
    print(f"{km} km = {meters:.2f} meters")
    print(f"{km} km = {centimeters:.2f} centimeters")
    print(f"{km} km = {millimeters:.2f} millimeters")

def main():
    while True:
        print("\nMars Telemetry Data Converter")
        print("Choose your unit of measurement:")
        print("1. Kilometers above Mars")
        print("2. Miles above Mars")

        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            try:
                km = float(input("Enter the number of kilometers above Mars: "))
                convert_kilometers(km)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "2":
            try:
                miles = float(input("Enter the number of miles above Mars: "))
                convert_miles(miles)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid selection. Please choose 1 or 2.")

if __name__ == "__main__":
    main()