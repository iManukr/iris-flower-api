# Iris Model Training

This folder contains the data and notebook used to train the Iris flower classifier that powers the API in [`../deployment`](../deployment).

## Contents

- `Iris_model.ipynb` - trains and tests the classifier.
- `Iris.csv` - Iris flower measurements used for training.
- `iris_model.joblib` - saved trained model used by the deployment API.
- `pyproject.toml` and `uv.lock` - reproducible Python dependencies.

## Run the notebook

From this folder, install the dependencies:

```powershell
uv sync
```

Then open `Iris_model.ipynb` in VS Code or Jupyter and run its cells in order. The notebook trains the model using sepal length, sepal width, petal length, and petal width, then saves the trained model as `iris_model.joblib`.

## Classes

The classifier predicts one of the following species:

- `Iris-setosa`
- `Iris-versicolor`
- `Iris-virginica`
