import calendar

# prints entire calendar of specified year
calendar.prcal(2023)

# prints first weekday. Default is 0 meaning Monday
print(calendar.firstweekday())

# returns true or false for leap year
print(calendar.isleap(2024))

# returns given month with each week as one list
print(calendar.monthcalendar(2023, 1))

# returns number of leap days from year1 to year2 not including year2
print(calendar.leapdays(2022, 2024))

# prints given month of given year
calendar.prmonth(2023, 2)
