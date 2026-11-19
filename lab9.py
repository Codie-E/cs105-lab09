import numpy as np
import matplotlib.pyplot as plt

days = np.array([1, 2, 3, 4, 5, 6, 7])
revenue = np.array([500, 600, 989, 700, 100, 600, 520])
costs = np.array([400, 250, 500, 700, 50, 200, 310])

print(days, revenue, costs)

profit = revenue - costs
print(profit)

mean = np.mean(profit)
max = np.max(profit)
min = np.min(profit)

print(mean, max, min)

plt.plot(days, profit)
plt.title("Daily Business Graph")
plt.xlabel("Days")
plt.ylabel("Profit")

plt.show()
