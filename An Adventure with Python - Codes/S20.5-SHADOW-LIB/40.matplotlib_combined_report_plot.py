import matplotlib.pyplot as plt

days_num = range(1, 11)
gold = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
xp = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]

# Plot two lines on one chart
plt.plot(days_num, gold, color="gold", label="Gold")
plt.plot(days_num, xp, color="purple", label="XP")

plt.legend()  # Show legend box
plt.show()
