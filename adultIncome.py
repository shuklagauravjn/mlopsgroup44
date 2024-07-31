import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

# Load the dataset
data = pd.read_csv('adult.csv')

# Display the first few rows of the dataset and the column names
print(data.head())
print(data.columns)

# Define feature columns and target column based on actual column names
feature_cols = ['age', 'workclass', 'education', 'marital-status', 'occupation', 'relationship', 'sex']
target_col = 'income'

# Correct column names to match dataset
feature_cols_corrected = [col.replace('-', '_') for col in feature_cols]

# Split the data into features (X) and target (y)
X = data[feature_cols_corrected]
y = data[target_col]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the preprocessing for numeric and categorical features
numeric_features = ['age']
numeric_transformer = StandardScaler()

categorical_features = ['workclass', 'education', 'marital_status', 'occupation', 'relationship', 'sex']
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Create a pipeline that first preprocesses the data and then applies a RandomForestClassifier
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Save the model to a file
dump(model, 'salary_predictor.joblib')
print('Model saved as salary_predictor.joblib')
