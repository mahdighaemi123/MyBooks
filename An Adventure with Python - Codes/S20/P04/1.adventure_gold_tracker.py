import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
gold = [100, 80, 50, 120, 200]

# Customizing the magic
plt.plot(days, gold, color='green', marker='o', linestyle='--')

# Adding labels (The Legend)
plt.title("My Gold Over Time")     # Title of the spell
plt.xlabel("Day of Adventure")     # X-axis label
plt.ylabel("Gold Coins")           # Y-axis label
plt.grid(True)                     # Add a grid for better reading

plt.show()
