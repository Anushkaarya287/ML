import numpy as np
import matplotlib.pyplot as plt
import os


X = np.array([
    [2104, 5, 1, 45],
    [1416, 3, 2, 40],
    [1534, 3, 2, 30],
    [852,  2, 1, 36]
], float)

y = np.array([460, 232, 315, 178], float)


Xb = np.column_stack([np.ones(len(X)), X])


beta = np.linalg.pinv(Xb) @ y
print("Correct Coefficients:", beta)


y_pred = Xb @ beta

os.makedirs("output", exist_ok=True)

# plot
plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred)
plt.plot([min(y), max(y)], [min(y), max(y)])
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Predicted vs Actual Price")

plt.savefig("output/predicted_vs_actual.png", dpi=300, bbox_inches="tight")

plt.show()
