def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = int(input("Choose the conversion type (1-6): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius is equal to {celsius_to_fahrenheit(celsius)} Fahrenheit")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit)} Celsius")
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius is equal to {celsius_to_kelvin(celsius)} Kelvin")
    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} Kelvin is equal to {kelvin_to_celsius(kelvin)} Celsius")
    elif choice == 5:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_kelvin(fahrenheit)} Kelvin")
    elif choice == 6:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} Kelvin is equal to {kelvin_to_fahrenheit(kelvin)} Fahrenheit")
    else:
        print("Invalid choice. Please select a valid option.")

main()
