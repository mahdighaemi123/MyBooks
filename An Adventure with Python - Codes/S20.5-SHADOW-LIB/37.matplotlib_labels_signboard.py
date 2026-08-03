import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed"]
temp = [20, 22, 19]

plt.plot(days, temp)
plt.title("Weather Report")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()
