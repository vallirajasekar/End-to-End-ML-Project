from flask import Flask
import os
#from src.mlProject.logging import * 
from mlProject.logging import *

#src/mlProject/logging/__init__.py
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    
     logging.info("We are testing our logging Module")
     return "Practice Make Man Perfect"
     

if __name__=='__main__':
   app.run(debug=True,port=5000)

