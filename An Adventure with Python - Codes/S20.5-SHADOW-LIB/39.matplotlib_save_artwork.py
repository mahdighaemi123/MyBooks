import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed"]
temp = [20, 22, 19]

plt.plot(days, temp)
plt.savefig("my_masterpiece.png")
print("Saved!")
