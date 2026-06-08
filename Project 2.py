# ──────────────────────────────────────────
#  Project 2: Simple Classification Model using AI —
# ──────────────────────────────────────────

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ── 1. Dataset Load
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

print("=" * 50)
print("  Dataset: Iris")
print("=" * 50)
print(df.head(10).to_string(index=False))
print(f"\nShape     : {df.shape}")
print(f"Classes   : {list(iris.target_names)}")
print(f"Missing   : {df.isnull().sum().sum()}")

# ── 2. Features aur Target alag karo ──────
X = df.drop('species', axis=1)   # features
y = df['species']                 # label

# ── 3. Train / Test Split ──────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\n[Split] Train: {len(X_train)}  |  Test: {len(X_test)}")

# ── 4. Normalize (Feature Scaling) ─────────
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ── 5. Model Banao aur Train Karo ──────────
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print(f"\n[Model] KNeighborsClassifier(k=3) trained ✓")

# ── 6. Predict ─────────────────────────────
y_pred = model.predict(X_test)

# ── 7. Evaluate ────────────────────────────
acc = accuracy_score(y_test, y_pred)
print(f"\n[Accuracy] {acc * 100:.1f}%")

print("\n[Classification Report]")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("[Confusion Matrix]")
cm = confusion_matrix(y_test, y_pred)
cm_df = pd.DataFrame(cm, index=iris.target_names, columns=iris.target_names)
print(cm_df)

# ── 8. Naye Sample pe Predict ──────────────
print("\n[Demo] Naya sample predict karo: [5.1, 3.5, 1.4, 0.2]")
sample = scaler.transform([[5.1, 3.5, 1.4, 0.2]])
pred   = model.predict(sample)[0]
print(f"       → Class: {iris.target_names[pred]}")

print("\n" + "=" * 50)
