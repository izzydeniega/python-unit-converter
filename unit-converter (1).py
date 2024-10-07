def unit_selection():
    print("Available conversions:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    
    choice = input("Enter the number of your choice (1-4): ")
    return choice

def conversion(choice, value):
    if choice == '1':
        return value * 0.621371, "km", "miles"
    elif choice == '2':
        return value * 1.60934, "miles", "km"
    elif choice == '3':
        return (value * 9/5) + 32, "°C", "°F"
    elif choice == '4':
        return (value - 32) * 5/9, "°F", "°C"
    else:
        return None, None, None

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        choice = unit_selection()
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue
        
        value = float(input("Enter the value to convert: "))
        
        result, from_unit, to_unit = conversion(choice, value)
        
        if result is not None:
            print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        else:
            print("An error occurred during conversion.")
        
        again = input("Do you want to perform another conversion? (yes/no): ")
        if again.lower() != 'yes':
            break
    
    print("Thank you for using the Unit Converter!")

if __name__ == "__main__":
    main()
