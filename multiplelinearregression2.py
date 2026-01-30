import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# load dataset
data = pd.read_csv("iot_sensor_data.csv")
X = data[['Humidity(%)', 'Light_Intensity(lx)', 'Motion']]
y = data['Temperature(C)']



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("R² Score:", r2_score(y_test, y_pred))

# plot:
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()])

plt.xlabel("Actual Temperature")
plt.ylabel("Predicted Temperature")
plt.title("Multiple Linear Regression: Actual vs Predicted")
plt.grid(True)

plt.show()
