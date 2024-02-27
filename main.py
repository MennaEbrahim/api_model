# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:34:52 2024

@author: menna
"""

#pip install fastapi uvicorn

# 1. Library imports
import uvicorn ##ASGI
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To my model': f'{name}'}



# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '_main_':
 
    uvicorn.run(app, host='127.0.0.1', port=8001)

#uvicorn app:app --reload