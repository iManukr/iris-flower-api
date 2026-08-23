# Iris Flower Prediction API

This project trains an Iris flower classifier and serves predictions through a FastAPI application.

## Project structure

- `iris/` — dataset, training notebook, and model-training project files.
- `deployment/` — FastAPI service, trained model, API README, and GitHub publishing guide.

## Run the API

```powershell
cd deployment
uv sync
uv run python main.py
```

Visit `http://127.0.0.1:8000/docs` to test the prediction API interactively.

See [the deployment README](deployment/README.md) for the request format and examples.
