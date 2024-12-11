import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression  # Replace with your model

# Load data from Excel file
file_path = r'C:\Users\singh\Desktop\Book1.xlsx'
df = pd.read_excel(file_path)

# Assuming your DataFrame has columns 'Actual' and 'Predicted'
X = df.drop('Actual', axis=1)  # Features
y_actual = df['Actual']  # Actual labels

# Split data into train and test sets (adjust test_size and random_state as needed)
X_train, X_test, y_train, y_test = train_test_split(X, y_actual, test_size=0.2, random_state=42)

# Train your model (replace with your model and fitting process)
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Create a confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Display the confusion matrix
print("Confusion Matrix:")
print(conf_matrix)
