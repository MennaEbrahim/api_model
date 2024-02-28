# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:27:29 2024

@author: menna
"""

import uvicorn
from fastapi import FastAPI
from Packages import Packages
import numpy as np
import pickle
import pandas as pd

app=FastAPI()
pickle_in=open("model9.pkl","rb")
model=pickle.load(pickle_in)
@app.get('/')
def index():
    return {'message':'Hello,world'}

@app.get('/{name}')
def get_name(name: str):
    return {'welcome to my model': f'Hello,{name}'}
@app.post('/predict')
def predict_packages(data:Packages):
   data=data.dict()
   january=data['january']
   
   february=data['february']
  
   march=data['march']
  
   april=data['april']
   
   may=data['may']
   
   june=data['june']
   
   july=data['july']
   
   august=data['august']

   septemper=data['septemper']

   october=data['october']
  
   november=data['november']

   december=data['december']
   
   kind=data['kind']
   
   #print(kind)
   
   #print(Average)
   # print(model.predict([[january,february,march,april,may,june,july,augest,septemper,october,november,kind,Average]]))
  #  print("Hello")
   prediction=model.predict([[january,february,march,april,may,june,july,august,septemper,october,november,december,kind]])
    
   return {"prediction": int(prediction[0])}

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
        



