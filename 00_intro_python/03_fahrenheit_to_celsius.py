"""
Program : Farenheit to Celsius Conversion
_________________________________________

This program promts users for Temperature in Farenheit and 
then outputs the temperature in Celcius
"""
def main():
    temp_farenheit : str = input("Enter temperature in Fahrenheit: ")
    temp_farenheit : int = int(temp_farenheit)
    temp_celcius : float = (temp_farenheit - 32) * 5.0/9.0
    print(f"Temperature: {temp_farenheit} = {temp_celcius}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()