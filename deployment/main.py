from pathlib import Path

import joblib
import pandas
import uvicorn

from fastapi import FastAPI, Form 
app = FastAPI()


MODEL_PATH = Path(__file__).with_name("iris_model.joblib")
loaded_model = joblib.load(MODEL_PATH)


FEATURES = [ 
    "SepalLengthCm", 
    "SepalWidthCm", 
    "PetalLengthCm",
    "PetalWidthCm"
]

FLOWER_NAMES = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica",
}


@app.get("/")
def root():
    return {
        "message": "Iris Flower Prediction API is running.",
        "docs": "/docs",
        "predict_endpoint": "/predict",
    }


@app.post("/predict")
def predict_flower(
    sepal_length: float = Form(), 
    sepal_width: float = Form(),
    petal_length: float = Form(),
    petal_width: float = Form()
    ): 


    new_flower  = pandas.DataFrame(
        [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
        ]], 
        columns= FEATURES

        )
    prediction = int(loaded_model.predict(new_flower)[0])


    return { 
        "Predicted Flower": FLOWER_NAMES[prediction]

    }

@app.post("/login")
def login(username: str = Form(), 
          password: str = Form()):
    return  {
       "username" :username,
       "password" : password
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
