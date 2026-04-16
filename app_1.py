from schema.user_input import Data
from fastapi import FastAPI  
from fastapi.responses import JSONResponse 
from schema.predicting_reaponse import PredictResponse
from models.predict import predict_output , model , MODEL_VERSION
from sqlalchemy.orm import  sessionmaker
from DataBase.db import User  , engine 
from schema.conversions import prediction_to_json
import pandas as pd 

## for database 
Session = sessionmaker(bind = engine) 
session = Session()

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
        import numpy as np

        # type conversion 
        age = int(data.age)
        weight = float(data.weight) 
        height = float(data.height ) 
        income_lpa = float(data.income_lpa) 
        bmi = float(data.bmi) 
        city_tier = float(data.city_tier)

        data = User( age    = age  , 
                    weight  =  weight, 
                    height  =   height , 
                    income_lpa = income_lpa ,        
                    smoker  =    data.smoker  , 
                    city    =    data.city  ,
                    occupation = data.occupation , 
                    Prediction = prediction  , 
                    bmi  = bmi  , 
                    lifestyle_risk = data.lifestyle_risk , 
                    age_group  =  data.age_group , 
                    city_tier  = city_tier ) 

        session.add(data) 
        session.commit()

        return JSONResponse(status_code=200 , content={"predicted Category" :   prediction } )
    
    except Exception as e : 
        return JSONResponse(status_code=500 , content=str(e)) 




@app.get('/data') 
def see_data() : 
    data = session.query(User).all()
    data = [prediction_to_json(u    ) for u in data ]
    return JSONResponse(status_code=200 , content= data )

    
