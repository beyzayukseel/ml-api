from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import sklearn

app = FastAPI()

def getResult(result):
    if(result == 0):
        return "IYI"
    elif(result == 1):
        return "ORTA"
    else:
        return "KOTU"

class StudentInfo(BaseModel):
    age:int
    gender:bool
    number_of_siblings:int
    weekly_tv_watch_hour:int
    weekly_play_pc_game_hour:int
    life_pleasure:int
    average_games_score:int
    average_game_time_in_minute:int
    activity_click_count:int
    activity_view_count:int
    activity_view_time_in_minute:int
    Anne:bool
    Baba:bool
    Ilkokul:bool
    Lise:bool
    OkumaYazmaBilmiyor: bool
    Ortaokul: bool
    Universite:bool
    
        
with open('/Users/random-forest.pkl','rb') as f:  
    model = pickle.load(f) 

@app.post('/')
async def deneme(item: StudentInfo):
    df = pd.DataFrame([item.model_dump()])
    predict = model.predict(df)
    result = getResult(int(predict))
    return {"prediction": result}
