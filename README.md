# FastAPI - fastML

That repository contains an API to send request our Random Forest Classification model.

FastAPI is a modern, fast, web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be easy to use and to enable the development of high-performance APIs quickly.

<br>

##### USED LIBRARIES:
<br>

```
    FastAPI
    BaseModel
    pickle
    pandas
    sklearn
```



##### PICKLE:

The `pickle` module is frequently used to package (serialize) and store machine learning models in Python.
  
``` 
import pickle
with open('random-forest.pkl', 'wb') as file:
    pickle.dump(rfc, file)
```


##### RUN COMMANDS:

```
python -m venv fastml
source fastml/bin/activate (mac) or  .\fastml\Scripts\activate (windows)
pip install uvicorn gunicorn fastapi pydantic sklearn pandas
uvicorn random-classifier-api:app --reload
```

##### EXAMPLE REQUEST:


```
curl --location 'http://localhost:8000/' \
--header 'Content-Type: application/json' \
--data '{
    "age":7,
    "gender":0,
    "number_of_siblings":4,
    "weekly_tv_watch_hour": 3,
    "weekly_play_pc_game_hour":4,
    "life_pleasure":5,
    "average_games_score":80,
    "average_game_time_in_minute":15,
    "activity_click_count":30,
    "activity_view_count":65,
    "activity_view_time_in_minute":20,
    "Anne":false,
    "Baba":true,
    "Ilkokul":false,
    "Lise":false,
    "OkumaYazmaBilmiyor": true,
    "Ortaokul": true,
    "Universite":false
}'

```

