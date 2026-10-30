import pandas as pd 

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# load the dataset
iris = load_iris()

x = pd.DataFrame(
    iris.data,
    columns=iris.feature_names 
)

y = iris.target

print("Dataset loaded successfully!")
print("Dataset shape:", x.shape)

#clean and prepare the data
print("\nMissiong values:")
print(x.isnull().sum())

print("\nDuplicate feature rows:", x.duplicated().sum())

#slip the dataset
x_train, x_test, y_train, y_test =train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:",len(x_train))
print("Testing sample:",len(x_test))

# Create and train the model 
model = DecisionTreeClassifier(random_state=42)

model.fit(x_train, y_train)

print("\nModel trainining completed!")

# make prediction
y_pred = model.predict(x_test) 

#Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)

# Predict a new flower
new_flower = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=iris.feature_names

)

prediction = model.predict(new_flower)

predicted_species  = iris.target_names[prediction[0]]

print("\nPredicted flower species:",predicted_species)
