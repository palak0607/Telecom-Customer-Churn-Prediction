from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle

model = pickle.load(open("model.pkl","rb"))

app = FastAPI()

class Input(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float
    Tenure: int
    
@app.get("/")
def read_root():
    return {"msg":"Customer Churn Predictor"}

@app.post("/predict")
def predict(input:Input):
    data= input
    data_in = [
        [
            data.gender, data.SeniorCitizen, data.Partner, data.Dependents,
            data.PhoneService, data.MultipleLines, data.InternetService, data.OnlineSecurity,
            data.OnlineBackup, data.DeviceProtection, data.TechSupport, data.StreamingTV,
            data.StreamingMovies, data.Contract, data.PaperlessBilling, data.PaymentMethod,
            data.MonthlyCharges, data.TotalCharges, data.Tenure
        ]
    ]
    prediction = model.predict(data_in)
    return{
        'prediction':  prediction.tolist()
    }
    
if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)