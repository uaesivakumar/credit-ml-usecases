import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Example dataset of transactions with amount and time difference
transactions = pd.DataFrame({
    'amount': [100, 200, 50, 10000, 70, 150, 80, 9000, 120, 60],
    'transaction_time_diff': [30, 45, 20, 5, 25, 40, 35, 3, 30, 20]
})

# Scale features for isolation forest
scaler = StandardScaler()
X_scaled = scaler.fit_transform(transactions)

# Fit IsolationForest to detect anomalies (fraud)
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_scaled)

# Predict anomalies
transactions['anomaly_score'] = model.decision_function(X_scaled)
transactions['is_fraud'] = model.predict(X_scaled)

# Convert prediction labels (-1 indicates anomaly) to boolean
transactions['is_fraud'] = transactions['is_fraud'] == -1

print(transactions)
