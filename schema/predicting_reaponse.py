from pydantic import BaseModel , Field
from typing import Dict


class PredictResponse(BaseModel) : 
    predicted_category : str = Field(..., description= "Prediction Category " , examples=['low' , 'medium' , 'high' ])

    confidence : float = Field(..., description= "Model's confidence score for the predicted classes range 0 to 1 " , example=8.2234)

    class_probability : Dict[str ,float ] = Field(..., description="Probability Distribution across all  possible Classes" , example= {'low' :0.3 , 'medium' : 0.7 ,'high':0.9})