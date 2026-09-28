print("Convert The Temperature")

conversion_choice = input(
    "Choose the converter (Celsius/Fahrenheit): "
).lower()

input_temperature = float(input("Enter the temperature: "))


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit:", fahrenheit)


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print("Celsius:", celsius)


if conversion_choice == "celsius":
    convert_celsius_to_fahrenheit(input_temperature)

elif conversion_choice == "fahrenheit":
    convert_fahrenheit_to_celsius(input_temperature)

else:
    print("Invalid choice.")

