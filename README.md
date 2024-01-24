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



