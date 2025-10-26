import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Sample dataset for credit risk modelling
data = {
    'credit_score': [750, 620, 680, 710, 590, 640, 700, 660],
    'credit_limit_utilization': [0.3, 0.8, 0.6, 0.4, 0.9, 0.7, 0.5, 0.6],
    'days_employed': [200, 1500, 800, 400, 1800, 1200, 300, 900],
    'default': [0, 1, 0, 0, 1, 1, 0, 0]
}

# Create a DataFrame
df = pd.DataFrame(data)
X = df[['credit_score', 'credit_limit_utilization', 'days_employed']]
y = df['default']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Print classification report
print(classification_report(y_test, y_pred))
