import datetime

# Format: Year, Month, Day
my_date = datetime.date(2000, 5, 15) 

# Get the full English name of the weekday
print(my_date.strftime("%A"))
