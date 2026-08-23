# Iris Flower Prediction API

A FastAPI service that predicts an Iris flower species from its sepal and petal measurements.

## Requirements

- Python 3.14 or later
- [uv](https://docs.astral.sh/uv/)

## Run locally

From this directory, install the dependencies and start the API:

```powershell
uv sync
uv run python main.py
```

The server runs at `http://127.0.0.1:8000`. Open the base URL to confirm it is running, or open `http://127.0.0.1:8000/docs` to use the interactive API documentation.

## Predict a flower

Send a `POST` request to `/predict` with the four measurements:

```powershell
curl.exe -X POST http://127.0.0.1:8000/predict `
  -F "sepal_length=5.1" `
  -F "sepal_width=3.5" `
  -F "petal_length=1.4" `
  -F "petal_width=0.2"
```

Example response:

```json
{
  "Predicted Flower": "Iris-setosa"
}
```

Possible predictions are `Iris-setosa`, `Iris-versicolor`, and `Iris-virginica`.

## Login endpoint

The service also includes a simple form endpoint:

```powershell
curl.exe -X POST http://127.0.0.1:8000/login `
  -F "username=example" `
  -F "password=secret"
```

## Add to Git

From the repository root:

```powershell
git add deployment
git commit -m "Add Iris prediction API"
```
