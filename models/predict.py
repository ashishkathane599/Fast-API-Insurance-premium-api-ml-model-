import pandas as pd 
import pickle 
import os

 ## import model 
# with open('D:\programing\AI-ML\Projects\Insurance_premium_api\models\model.pkl' , 'rb') as f : 
#     model = pickle.load(f) 
# to avoid a error regarding the file path in docker 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)
# Model version (genraly track  using MLFlow)  
MODEL_VERSION = '1.0.0'        # manual 

# get Class labels from model 
class_labels = model.classes_.tolist() 


def predict_output(user_input) : 
    
    input_df = pd.DataFrame([user_input])

    output = model.predict(input_df)[0]

    # get probabilities for all classes ['high' , 'low' , 'medium' ]
    probabilities = model.predict_proba(input_df)[0] 
    confidence = max(probabilities)

    # create mapping {class_name :  probablitity }
    class_probs = dict(zip(class_labels , map(lambda p: round(p,4) , probabilities)))
    
    return { 
        "predicted_category" : output , 
        "confidence" : round(confidence,4 ) , 
        "class_probability " : class_probs 
    }