def convert_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def get_temperature_input():
  """Prompts the user for temperature and unit, handles errors."""
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
      if unit not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
      return temperature, unit
    except ValueError:
      print("Invalid input. Please enter a numeric temperature and 'C' or 'F'.")

def main():
  temperature, unit = get_temperature_input()

  if unit == 'C':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp}°F")
  elif unit == 'F':
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")

if __name__ == "__main__":
  main()