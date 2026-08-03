# --- The Quest Deadline Notifier ---

# 1. Summon the magic (Library)
# We import the datetime module to handle dates
import datetime

# 2. Get the current date (The "Now" Spell)
# datetime.datetime.now() gets the exact current moment
today = datetime.datetime.now()

# 3. Create the duration (The "Time Travel Ticket")
# timedelta allows us to define a span of time (days, hours, etc.)
one_week = datetime.timedelta(days=7)

# 4. Calculate the future (The Math)
# Just add the duration to the current date!
deadline = today + one_week

# 5. Format the scrolls (Beautification)
# We use .strftime() to convert ugly computer time to readable text
# %A = Day Name, %B = Month Name, %d = Day Number
today_formatted = today.strftime("%A, %B %d")
deadline_formatted = deadline.strftime("%A, %B %d")

# 6. Display the results
print("--- Quest Master's Log ---")
print(f"Quest assigned on: {today_formatted}")
print(f"Quest deadline is: {deadline_formatted}")
print("============================")
