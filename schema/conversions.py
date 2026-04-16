# tables to json  
""" Used to convert a table into json """
def prediction_to_json(data ):
    return {
        "age": data.age,
        "weight": data.weight,
        "height": data.height,
        "income_lpa": data.income_lpa,
        "smoker": data.smoker,
        "city": data.city,
        "occupation": data.occupation,
        "Prediction": data.Prediction,
        "bmi": data.bmi,
        "lifestyle_risk": data.lifestyle_risk,
        "age_group": data.age_group,
        "city_tier": data.city_tier
    }




if __name__ == '__main__' :
    data = {
    "age": 1,
    "weight": 1,
    "height": 1,
    "income_lpa": 1,
    "smoker": True,
    "city": "String",
    "occupation": "retired",
    "Prediction": {
      "predicted_category": "Medium",
      "confidence": 0.65,
      "class_probability ": {
        "High": 0.24,
        "Low": 0.11,
        "Medium": 0.65
      }
    },
    "bmi": 1,
    "lifestyle_risk": "medium",
    "age_group": "young",
    "city_tier": 3
   }

   
