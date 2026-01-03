import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
df = pd.read_csv("loan_data.csv")
df.head()
# categorical
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)

# numerical
df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
Q1 = df['LoanAmount'].quantile(0.25)
Q3 = df['LoanAmount'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['LoanAmount'] >= lower) & (df['LoanAmount'] <= upper)]
sns.countplot(x='Loan_Status', data=df)
plt.show()

sns.boxplot(x='Loan_Status', y='LoanAmount', data=df)
plt.show()
df = pd.get_dummies(df, drop_first=True)
X = df.drop('Loan_Status_Y', axis=1)
y = df['Loan_Status_Y']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
