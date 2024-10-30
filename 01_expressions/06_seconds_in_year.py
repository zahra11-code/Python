"""Problem: Seconds in Year
___________________________
Description: Use Python to calculate the number of seconds in a year, 
and tell the user what the result is in a nice print statement that looks like this
(of course the value 5 should be the calculated number instead):
There are 5 seconds in a year!

You should use constants for this exercise
-- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.
"""
DAYS_IN_A_YEAR : int = 365
HOURS_IN_A_DAY :int = 24
MINUTES_IN_A_HOUR : int = 60
SECONDS_IN_A_HOUR :int = 60 
def main():
    seconds_in_a_year : int = DAYS_IN_A_YEAR * HOURS_IN_A_DAY * MINUTES_IN_A_HOUR * SECONDS_IN_A_HOUR
    print(f"There are {seconds_in_a_year} seconds in a year!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()