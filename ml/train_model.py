from sklearn.ensemble import IsolationForest
from ml.dataset_generator import generate_data

df = generate_data()

model = IsolationForest(contamination=0.05)
model.fit(df[["call_duration", "cost"]])

print("Model trained")
