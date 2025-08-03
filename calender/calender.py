import calendar
from datetime import date


year = date.today().year
month = date.today().month


cal = calendar.month(year, month)

months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december",]

short_month = ["jan", "feb", "mar", "apr", "may", "jun",
               "jul", "aug", "sep", "oct", "nov", "dec",]

numeric_month = ["1", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "11", "12",]

"""
print("This month")
print(cal)
"""

while True:

    print("\ninput next to see next month or prev to see previous month or enter the month you want or "
          "input \"year\" to select year of your choice")

    user_input = input("Move to a certin month: ").lower()

    if user_input == "next":
        month += 1
        cal = calendar.month(year, month)
        print(cal)

    elif user_input == "prev":
        month -= 1
        cal = calendar.month(year, month)
        print(cal)

    elif user_input in months:
        month = (months.index(user_input))+1
        cal = calendar.month(year, month)
        print(cal)

    elif user_input in short_month:
        month = (short_month.index(user_input))+1
        cal = calendar.month(year, month)
        print(cal)

    elif user_input == "sept":
        month = 9
        cal = calendar.month(year, month)
        print(cal)

    elif user_input in numeric_month:
        month = int(user_input)
        cal = calendar.month(year, month)
        print(cal)

    elif user_input == "year":
        year_input = input("Input year of your choice: ").lower()
        year = int(year_input)
        cal = calendar.month(year, month)
        print(cal)

    else:
        print("Invalid input!")
