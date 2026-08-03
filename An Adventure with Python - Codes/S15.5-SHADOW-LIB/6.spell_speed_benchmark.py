import datetime

# Capture start time
start = datetime.datetime.now()

# A heavy loop simulation (1 million iterations)
for i in range(1000000):
    pass

# Capture end time
end = datetime.datetime.now()

print(f"Time taken: {end - start}")
