import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, label_binarize
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_curve, auc

# load data
data = pd.read_csv("../Iris.csv")

if 'Id' in data.columns:
    data.drop('Id', axis=1, inplace=True)

X = data[['SepalLengthCm', 'SepalWidthCm']]
y = data['Species']

# encode labels
le = LabelEncoder()
y = le.fit_transform(y)

# binarize labels
y_bin = label_binarize(y, classes=[0, 1, 2])

# train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_bin, test_size=0.2, random_state=42
)

# scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# models
models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "SVM": SVC(probability=True),
    "LDA": LinearDiscriminantAnalysis(),
    "KNN": KNeighborsClassifier()
}

# ensure output folder exists
os.makedirs("output", exist_ok=True)

# plot ROC curves
plt.figure(figsize=(8, 6))

for name, model in models.items():
    model.fit(X_train, y_train.argmax(axis=1))

    if hasattr(model, "predict_proba"):
        y_score = model.predict_proba(X_test)
    else:
        y_score = model.decision_function(X_test)

    fpr, tpr, _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.2f})")

# diagonal reference line
plt.plot([0, 1], [0, 1], 'k--')

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves for Iris Classification")
plt.legend()

# save plot
plt.savefig("output/iris_roc_curves.png", dpi=300, bbox_inches="tight")
plt.show()

print("ROC curve image saved successfully in output folder")
