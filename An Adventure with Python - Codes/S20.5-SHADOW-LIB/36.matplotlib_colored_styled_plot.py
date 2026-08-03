import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed"]
temp = [20, 22, 19]

# Red line, Star markers, Dashed line
plt.plot(days, temp, color='red', marker='*', linestyle='--')
plt.show()
