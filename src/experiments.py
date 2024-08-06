import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from mlflow.tracking._tracking_service.utils import get_tracking_uri, set_tracking_uri

from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import itertools
import joblib  # For saving the model to a file

# Load and preprocess dataset
dataset = pd.read_csv('/Users/gauravshukla/bits/python/data/adult.csv')

le = LabelEncoder()
dataset['income'] = le.fit_transform(dataset['income'])
dataset = dataset.replace('?', np.nan)

columns_with_nan = ['workclass', 'occupation', 'native.country']
for col in columns_with_nan:
    dataset[col] = dataset[col].fillna(dataset[col].mode()[0])

dataset['marital.status'] = dataset['marital.status'].map({
    'Married-civ-spouse': 1,
    'Never-married': 2,
    'Divorced': 3,
    'Separated': 4,
    'Widowed': 5,
    'Married-spouse-absent': 6,
    'Married-AF-spouse': 7
})

for col in dataset.columns:
    if dataset[col].dtypes == 'object':
        encoder = LabelEncoder()
        dataset[col] = encoder.fit_transform(dataset[col])

X = dataset.drop('income', axis=1)
Y = dataset['income']
X = X.drop(['workclass', 'education', 'race', 'sex',
            'capital.loss', 'native.country', 'fnlwgt', 'relationship',
            'capital.gain'], axis=1)

scaler = StandardScaler()
X = scaler.fit_transform(X)

ros = RandomOverSampler(random_state=42)
X_resampled, Y_resampled = ros.fit_resample(X, Y)

# Define parameter grid for experimentation
param_grid = {
    'RandomForestClassifier': {
        'model': RandomForestClassifier,
        'params': {
            'max_depth': [10, 20, 30, 50],
            'n_estimators': [50, 100, 150]
        }
    },
    'GradientBoostingClassifier': {
        'model': GradientBoostingClassifier,
        'params': {
            'n_estimators': [50, 100, 150],
            'learning_rate': [0.01, 0.1, 0.2],
            'max_depth': [3, 5, 7]
        }
    },
    'LogisticRegression': {
        'model': LogisticRegression,
        'params': {
            'C': [0.1, 1, 10],
            'solver': ['lbfgs', 'liblinear']
        }
    }
}

# Initialize variables to track the best model
best_model = None
best_accuracy = 0
best_run_name = ""

# Set MLflow tracking URI
set_tracking_uri(r"http://127.0.0.1:5000")

# Run experiments
for model_name, model_info in param_grid.items():
    model_class = model_info['model']
    params_grid = model_info['params']

    # Generate all combinations of parameters
    param_names = list(params_grid.keys())
    param_combinations = [dict(zip(param_names, comb)) for comb in itertools.product(*params_grid.values())]

    for param_combination in param_combinations:
        # Ensure correct parameter types
        param_combination = {k: int(v) if isinstance(v, float) and v.is_integer() else v for k, v in
                             param_combination.items()}

        run_name = f"{model_name}_params_{'_'.join(f'{k}_{v}' for k, v in param_combination.items())}"
        with mlflow.start_run(run_name=run_name) as run:
            print(f"Experiment with model: {model_name}, params: {param_combination}")

            # Initialize and train the model
            model = model_class(**param_combination, random_state=42)
            model.fit(X_resampled, Y_resampled)

            # Evaluate the model
            Y_pred = model.predict(X_resampled)
            accuracy = accuracy_score(Y_resampled, Y_pred)

            # Log parameters and metrics
            for param, value in param_combination.items():
                mlflow.log_param(param, value)
            mlflow.log_metric("accuracy", accuracy)
            mlflow.sklearn.log_model(model, "model")

            # Log the dataset as an artifact
            mlflow.log_artifact('/Users/gauravshukla/bits/python/data/adult.csv')

            # Optionally log an example prediction
            example_input = np.array([[20, 10, 3, 5, 40]])
            example_input_scaled = scaler.transform(example_input)
            example_prediction = model.predict(example_input_scaled)
            mlflow.log_metric("example_prediction", example_prediction[0])

            print(f"Logged run with model: {model_name} and params: {param_combination}")

            # Update the best model if current one is better
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_model = model
                best_run_name = run_name

# Save the best model to a file
if best_model:
    joblib.dump(best_model, 'best_model.pkl')
    print(f"Best model saved to best_model.pkl with accuracy: {best_accuracy}")

print(f"MLflow Tracking URI: {get_tracking_uri()}")
print("All experiments completed.")
