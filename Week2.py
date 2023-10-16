def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Welcome to the Temperature Converter!")
print("Options:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

option = int(input("Select an option (1/2): "))
try:
    if option == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}Â°C is equal to {fahrenheit:.2f}Â°F")
    elif option == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}Â°F is equal to {celsius:.2f}Â°C")
    else:
        print("Invalid option. Please select 1 or 2.")
except ValueError:
        print("invalid input, please enter a valid number")
