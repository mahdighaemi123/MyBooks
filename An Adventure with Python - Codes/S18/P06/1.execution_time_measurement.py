import time

# Record the start time
start_time = time.time()

# ... The spell runs here ...
# (Example: Count to 1,000,000)
x = 0
for i in range(1000000):
    x += 1

# Record the end time
end_time = time.time()

# Calculate duration
duration = end_time - start_time
print(f"The spell took {duration} seconds.")