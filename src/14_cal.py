"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
    `14_cal.py month [year]`
and does the following:
    - If the user doesn't specify any input, your program should
      print the calendar for the current month. The 'datetime'
      module may be helpful for this.
    - If the user specifies one argument, assume they passed in a
      month and render the calendar for that month of the current year.
    - If the user specifies two arguments, assume they passed in
      both the month and the year. Render the calendar for that
      month and year.
    - Otherwise, print a usage statement to the terminal indicating
      the format that your program expects arguments to be given.
      Then exit the program.
"""

import sys
import calendar
from datetime import datetime

def main():

    def confirm_month(month):
        months = [None, 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        # If the month is a number, return that number.
        if type(month) == int: return month
        # otherwise, return the integer of the index in the 'months' array.
        return months.index(month.lower())
    try:
        # Use the given month/year if the user gave it. If it's NOT given, take today's month/year. 
        month = confirm_month(sys.argv[1]) if len(sys.argv) > 1 else datetime.today().month
        year  = int(sys.argv[2])           if len(sys.argv) > 2 else datetime.today().year

        newCalendar = calendar.TextCalendar()
        newCalendar.prmonth(year, month)
    except:
        # If the function isn't called properly, output this help message.
        print("\nPlease call this function with the proper format:")
        print(f'{sys.argv[0]} [month,[ year]]')
        print(f'\nYou can call this function without a month or year,\nand it will print the current month\'s calendar')
        print(f'\nThe month can be either:\n- The full month name\n- The index of the month(from 1-12)')
        print(f'The Year must be the full year (1997, 2020, etc)')
    


if __name__ == "__main__":
    main()