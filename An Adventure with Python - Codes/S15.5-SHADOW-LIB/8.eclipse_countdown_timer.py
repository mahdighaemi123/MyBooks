import datetime

now = datetime.datetime.now()
target_date = datetime.datetime(2030, 1, 1) # Set a future date

# Calculate remaining time (Time Delta)
remaining = target_date - now
print(f"Time left: {remaining}")
