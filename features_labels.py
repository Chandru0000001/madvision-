import pandas as pd

# Create a dataset
data = {
    "study_hours": [2, 6, 4, 1, 7],
    "attendance": [60, 90, 75, 50, 95],
    "previous_marks": [45, 85, 65, 30, 90],
    "final_result": ["Fail", "Pass", "Pass", "Fail", "Pass"]
}

df = pd.DataFrame(data)

# Display the complete dataset
print("Complete Dataset:")
print(df)

# Select features (inputs)
X = df[["study_hours", "attendance", "previous_marks"]]

# Select label (target)
y = df["final_result"]

print("\nFeatures:")
print(X)

print("\nLabels:")
print(y)