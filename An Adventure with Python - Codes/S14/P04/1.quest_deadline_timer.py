# We need both datetime and timedelta for this
import datetime

# Get the current moment
now = datetime.datetime.now()
print(f"Quest accepted on: {now.strftime('%Y-%m-%d')}")

# 1. Create a "duration" spell
quest_duration = datetime.timedelta(days=7)

# 2. Add the duration to the current date
deadline = now + quest_duration

print(f"Quest deadline is: {deadline.strftime('%Y-%m-%d')}")

# You can also travel to the past!
three_hours_ago = now - datetime.timedelta(hours=3)
print(f"We started 3 hours ago, at: {three_hours_ago.strftime('%H:%M')}")
