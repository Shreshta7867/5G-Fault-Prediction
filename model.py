import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("Balanced_5G_KPI__first_10_rows_.csv")

# Select features that actually exist in your CSV
X = df[[
    "latency_ms",
    "throughput_mbps",
    "jitter_ms",
    "error_rate",
    "cpu_usage_pct",
    "memory_usage_pct",
    "handover_success_rate",
    "packet_loss"
]]

y = df["fault"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model
joblib.dump(model, "fault_model.pkl")
print("Model saved as fault_model.pkl")
