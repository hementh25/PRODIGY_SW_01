def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit.lower() == 'celsius':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit.lower() == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit.lower() == 'kelvin':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        raise ValueError("Invalid unit. Please enter 'Celsius', 'Fahrenheit', or 'Kelvin'.")

def main():
    print("Temperature Converter")
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (Celsius, Fahrenheit, Kelvin): ")

    try:
        converted1, converted2 = convert_temperature(value, unit)
        if unit.lower() == 'celsius':
            print(f"{value} degrees Celsius is {converted1:.2f} degrees Fahrenheit and {converted2:.2f} Kelvin.")
        elif unit.lower() == 'fahrenheit':
            print(f"{value} degrees Fahrenheit is {converted1:.2f} degrees Celsius and {converted2:.2f} Kelvin.")
        elif unit.lower() == 'kelvin':
            print(f"{value} Kelvin is {converted1:.2f} degrees Celsius and {converted2:.2f} degrees Fahrenheit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()