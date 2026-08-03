import matplotlib.pyplot as plt
import numpy as np
  
# Generate random scores
scores = np.random.randint(0, 21, 100)
  
plt.hist(scores, bins=5)
plt.show()
