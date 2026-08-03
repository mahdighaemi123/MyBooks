import matplotlib.pyplot as plt

sizes = [40, 30, 30]
labels = ["Human", "Elf", "Dwarf"]
  
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
