from schema.user_input import Data
from fastapi import FastAPI  
from fastapi.responses import JSONResponse 
from schema.predicting_reaponse import PredictResponse
from models.predict import predict_output , model , MODEL_VERSION
import pandas as pd 


 



## fastapi  app 
app = FastAPI()


# ================================================= Fast API =====================================================

@app.get('/')   #  human readable 
def home() : 
    return { 'message' : 'Insurance Premium Prediction'}
    
@app.get('/health')   # for diployment purpuse ( machine readable ) for cloud 
def health_check() : 
    return {
        'Status' : 'OK' , 
        'version': MODEL_VERSION 
    } 



@app.post('/Predict' , response_model=PredictResponse) 
def predict_premium(data : Data) :   # Data is data validation class 
    input_df = {
        'bmi'       : data.bmi , 
        'age_group' : data.age_group , 
        'Lifestyle_risk' : data.lifestyle_risk, 
        'city_tier' : data.city_tier , 
        'income_lpa' : data.income_lpa , 
        'occupation' : data.occupation 
         }

    try : 
        prediction = predict_output(input_df) 

        return JSONResponse(status_code=200 , content={"predicted Category" :   prediction } )
    
    except Exception as e : 
        return JSONResponse(status_code=500 , content=str(e)) 

    
