def display_units():
    print("📡 Distance Unit Breakdown")
    choice = input("Would you like to enter miles or kilometers? (type 'miles' or 'kilometers'): ").strip().lower()

    if choice == "miles":
        try:
            miles = float(input("Enter distance in miles: "))
        except ValueError:
            print("❌ Invalid number.")
            return

        # Derived imperial units
        yards = miles * 1760
        feet = miles * 5280
        inches = miles * 63360

        print("\n📏 Imperial Units:")
        print(f"Miles: {miles}")
        print(f"Yards: {yards:.2f}")
        print(f"Feet: {feet:.2f}")
        print(f"Inches: {inches:.2f}")

    elif choice == "kilometers":
        try:
            kilometers = float(input("Enter distance in kilometers: "))
        except ValueError:
            print("❌ Invalid number.")
            return

        # Derived metric units
        meters = kilometers * 1000
        centimeters = kilometers * 100000
        millimeters = kilometers * 1_000_000

        print("\n📐 Metric Units:")
        print(f"Kilometers: {kilometers}")
        print(f"Meters: {meters:.2f}")
        print(f"Centimeters: {centimeters:.2f}")
        print(f"Millimeters: {millimeters:.2f}")

    else:
        print("❌ Invalid choice. Please type 'miles' or 'kilometers'.")

    print("\n✅ Display complete.")

if __name__ == "__main__":
    display_units()
