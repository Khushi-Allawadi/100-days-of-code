days = int(input("Enter the number of days in this year: "))
days_in_year = 365
days_in_leap_year = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

leap_year_result = days_in_leap_year * hours_in_day * minutes_in_hour * seconds_in_minute

if days == 366:
  print("It's a leap year!", leap_year_result)
else:
  print("It's not a leap year.", result)
  
