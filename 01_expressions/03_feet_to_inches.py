"""Problem: Feet to Inches
__________________________
Description: Converts feet to inches. Feet is an American unit of measurement.
 There are 12 inches per foot. Foot is the singular, and feet is the plural.
"""
def feet_to_inches(feet):
    inches = feet * 12
    return inches

def main():
    print("Convert Feet to Inches")
    feet = float(input("Enter number of feet: "))
    inches = feet_to_inches(feet)
    print(str(feet) + " is equal to " + str(inches))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()