from fastapi import FastAPI
import pandas as pd
import uvicorn
from src.pipeline.predict_pipeline import PredictionPipeline
from src.utils import read_config
from src import constant
from pydantic import BaseModel

config = read_config(filepath=constant.CONFIG_FILE).model_prediction
predict_pipe = PredictionPipeline(config=config)

class PredictionInputSchema(BaseModel):
    Age: int
    BusinessTravel: str
    Department: str
    EducationField: str
    EnvironmentSatisfaction: int
    Gender: str
    HourlyRate: int
    JobInvolvement: int
    JobSatisfaction: int
    MaritalStatus: str
    MonthlyIncome: int
    OverTime: str
    PerformanceRating: int
    TotalWorkingYears: int
    YearsAtCompany: int
    YearsSinceLastPromotion: int

app = FastAPI(name="AttriPred", description="I love pineapples")

@app.get("/infer")
async def infer(data: PredictionInputSchema):
    data = pd.DataFrame(data=data.model_dump(), index=[0])
    prediction = predict_pipe.predict(data=data)
    return {"prediction_class": "Yes" if prediction.argmax() == 1 else "No", "prediction_proba": prediction.squeeze().tolist()[prediction.argmax()], "model_metadata": predict_pipe}

if __name__ == "__main__":
    uvicorn.run(app=app, port=8000, host="0.0.0.0")