def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Leap Year")
    else:print("Not Leap Year")
is_leap_year(year=int(input('Enter a year: ')))
is_leap_year(year=int(input('Enter a year: ')))