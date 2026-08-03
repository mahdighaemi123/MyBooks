# speed_test.py
# The Great Race: Python Lists vs. NumPy Arrays

import numpy as np
import time

print("--- Generating Data for 1,000,000 Adventurers ---")

# 1. Create the NumPy Array (The Modern Army)
# Generates 1 million random numbers between 0 and 100
numpy_array = np.random.randint(0, 100, 1_000_000)

# 2. Create the Python List (The Traditional Backpack)
# We convert the array to a list so Python takes the "hard way" (for fairness)
python_list = list(numpy_array)

print("Data ready! Starting the race...\n")

# --- RACE 1: The Old Way (Python Loop) ---
# We start the stopwatch
start_time = time.time()

total_sum = 0
for score in python_list:
    total_sum += score

average_python = total_sum / len(python_list)

# We stop the stopwatch
end_time = time.time()
python_duration = end_time - start_time

print(f"Python Loop Result: {average_python}")
print(f"Python Time: {python_duration} seconds\n")


# --- RACE 2: The Modern Way (NumPy) ---
# We start the stopwatch again
start_time = time.time()

# NumPy calculates mean in ONE ultra-fast step (Vectorization)
average_numpy = np.mean(numpy_array)

# We stop the stopwatch
end_time = time.time()
numpy_duration = end_time - start_time

print(f"NumPy Result: {average_numpy}")
print(f"NumPy Time: {numpy_duration} seconds\n")


# --- The Verdict ---
# Calculate how many times faster NumPy was
speedup = python_duration / numpy_duration

print("------------------------------------------")
print(f"CONCLUSION: NumPy was {speedup} times faster!")
print("------------------------------------------")
