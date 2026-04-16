from sqlalchemy import create_engine , Column , Integer , String , Float , Boolean , JSON 
from sqlalchemy.orm import declarative_base  

## create an engine 
engine = create_engine('sqlite:///test.db' , echo=True )

# creating base to create a tables 
Base = declarative_base() 

# table 
class User(Base) : 
    __tablename__= "prediction_data" 

    Sr_No   =   Column(Integer , primary_key =True )
    age     =   Column(Float )  
    weight  =   Column(Float )
    height  =   Column(Float )
    income_lpa = Column(Float)
    smoker  =    Column(Boolean)
    city    =    Column(String)
    occupation = Column(String)
    Prediction = Column(JSON) 
    bmi  = Column(Float) 
    lifestyle_risk =Column(String) 
    age_group    = Column(String) 
    city_tier    = Column(Integer)

Base.metadata.create_all(engine)

