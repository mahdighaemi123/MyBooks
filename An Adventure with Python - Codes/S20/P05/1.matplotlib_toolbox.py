import matplotlib.pyplot as plt

# 1
plt.plot([1, 2, 3], [2, 4, 6])
plt.show()

# 2
plt.bar(['A', 'B'], [10, 20])
plt.show()

# 3
plt.scatter([20, 30, 40], [50, 45, 30])
plt.show()

# 4
scores = [10, 10, 20, 20, 20, 30]
plt.hist(scores, bins=3)
plt.show()

# 5
plt.pie([40, 60], labels=['Mages', 'Warriors'])
plt.show()

# 6
plt.title("Name")

# 7
plt.xlabel('Titles label')
plt.ylabel('Numbers label')

# 8
plt.figure(figsize=(10, 5))

# 9
plt.savefig("my_chart.png")

# 10
x = [1, 2, 3]
y1 = [10, 15, 20]  # Gold
y2 = [8, 12, 18]   # Silver

plt.plot(x, y1, label="Gold")
plt.plot(x, y2, label="Silver")
plt.legend()  # Shows the legend box
plt.show()