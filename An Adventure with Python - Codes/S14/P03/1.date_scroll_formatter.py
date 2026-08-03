import datetime

current_moment = datetime.datetime.now()

# Let's format this object into a readable string

# Simple format: YYYY-MM-DD like 2026-12-12
simple_date = current_moment.strftime("%Y-%m-%d")
print(f"Simple Date Scroll: {simple_date}")

# A more beautiful, adventurous format
fancy_date = current_moment.strftime("Today is %A, the %dth of %B, %Y")
print(f"Fancy Date Scroll: {fancy_date}")
