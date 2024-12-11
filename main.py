import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\GURMEJ SINGH\Desktop\MINI PROJECT GURMEJ SINGH\Dataset.csv")
df.head()

x = df.drop(['Date', 'addiction_ratio'], axis=1)
x = x.dropna()
y = df['addiction_ratio']

le = LabelEncoder()
categorical_columns = ['smoker', 'food_prob', 'sleeping', 'depression', 'confuision', 'forget', 
                       'relation', 'weight_loss', 'illness_other', 'economic']

for column in categorical_columns:
    x[column] = le.fit_transform(x[column])

assert x.isnull().sum().sum() == 0, "There are still missing values in the feature set"

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"Classification Report for {model.__class__.__name__}:\n{classification_report(y_test, predictions)}")
    print(f"Confusion Matrix for {model.__class__.__name__}:\n{confusion_matrix(y_test, predictions)}")
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy: {accuracy}")
    return accuracy

models = {
    "Logistic Regression": LogisticRegression(solver='lbfgs', max_iter=1500),
    "Gaussian Naive Bayes": GaussianNB(),
    "Decision Tree": tree.DecisionTreeClassifier(),
    "AdaBoost": AdaBoostClassifier(n_estimators=100, random_state=0),
    "MLP Classifier": MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
}

accuracies = []

for model_name, model in models.items():
    print(f"\nEvaluating {model_name}...")
    accuracy = evaluate_model(model, X_train, X_test, y_train, y_test)
    accuracies.append(accuracy)

plt.figure(figsize=(10, 6))
plt.bar(models.keys(), accuracies, color='skyblue')
plt.ylabel("Accuracy")
plt.xlabel("Models")
plt.title("Model Accuracy Comparison")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(models.keys(), accuracies, color='green')
plt.ylabel("Accuracy")
plt.xlabel("Models")
plt.title("Model Accuracy Comparison")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(models.keys(), accuracies, marker='o', linestyle='-', color='orange')
plt.ylabel("Accuracy")
plt.xlabel("Models")
plt.title("Model Accuracy Comparison")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(x.corr(), vmin=0, vmax=1, cmap='viridis', annot=True, fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['smoker'], color='black', linewidth=0.5, linestyle='dotted')
plt.xlabel('Age')
plt.ylabel('Smoker')
plt.title('Smoker vs Age')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['addiction_ratio'], color='black', linewidth=0.5, linestyle='dotted')
plt.xlabel('Age')
plt.ylabel('Addiction Ratio')
plt.title('Addiction Ratio vs Age')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.bar(df['age'], df['depression'], color='red', linewidth=0.5, linestyle='dotted')
plt.xlabel('Age')
plt.ylabel('Depression Ratio')
plt.title('Depression Ratio vs Age')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.bar(df['age'], df['economic'], color='blue', linewidth=0.5, linestyle='dotted')
plt.xlabel('Age')
plt.ylabel('Economic Ratio')
plt.title('Economic Ratio vs Age')
plt.tight_layout()
plt.show()
