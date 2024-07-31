import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

# Load the dataset
data = pd.read_csv('./data/adult.csv')

# Display the first few rows of the dataset and the column names
print(data.head())
print(data.columns)

# Based on the actual column names, update the feature columns and target column
feature_cols = ['age', 'workclass', 'education', 'marital-status', 'occupation', 'relationship', 'sex']
target_col = 'income'

# Check for actual column names in the dataset and make sure they match
actual_columns = list(data.columns)
print("Actual columns in the dataset:", actual_columns)

# Map provided feature columns to actual dataset columns
# Manually replace any discrepancies observed in the column names
column_mapping = {
    'age': 'age',
    'workclass': 'workclass',
    'education': 'education',
    'marital-status': 'marital-status',
    'occupation': 'occupation',
    'relationship': 'relationship',
    'sex': 'sex'
}

# Correct feature column names based on actual columns in the dataset
feature_cols_corrected = [column_mapping[col] for col in feature_cols]
print("Corrected feature columns:", feature_cols_corrected)

# Ensure the target column is correct
target_col_corrected = target_col
print("Corrected target column:", target_col_corrected)

# Select features and target from the dataset
X = data
