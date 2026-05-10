from pydantic import BaseModel

class InputData(BaseModel):
    Gender: float
    Age: float
    Academic_Pressure: float
    CGPA: float
    Study_Satisfaction: float
    Work_Study_Hours: float
    Financial_Stress: float
    City_Code: float
    Sleep_Duration_Code: float
    Dietary_Habits_Code: float
    Degree_Code: float
    Suicidal_Thoughts: float
    Family_History_Mental_Illness: float
    Profession_Code: float

#mariem-bilel
class LinearRegressionInput(BaseModel):
    Gender: float
    Age: float
    CGPA: float
    Study_Satisfaction: float
    Work_Study_Hours: float
    Financial_Stress: float
    City_Code: float
    Sleep_Duration_Code: float
    Dietary_Habits_Code: float
    Degree_Code: float
    Suicidal_Thoughts: float
    Family_History_Mental_Illness: float
    Profession_Code: float
    Depression: float  
