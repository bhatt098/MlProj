import pickle
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from src.exception import CustomException
import sys

application=Flask(__name__)

app=application

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        
       if request.method=='GET':
           return render_template('home.html')
       else:
           data=CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=request.form.get('reading_score'),
                writing_score=request.form.get('writing_score')
                )
           
           dataFrame=data.get_data_as_dataframe()
           print(dataFrame)
           predict=PredictPipeline()
           results=predict.predict(dataFrame)
           return render_template('home.html',results=results[0])
       
    except Exception as e:
        raise CustomException(e,sys)
        
        
if __name__=='__main__':
    app.run(debug=True)
    
    
#  self.gender=gender,
#         self.race_ethnicity=race_ethnicity,
#         self.parental_level_of_education=parental_level_of_education,
#         self.lunch=lunch,
#         self.test_preparation_course=test_preparation_course,
#         # self.math_score=math_score,
#         self.reading_score=reading_score,
#         self.writing_score=writing_score
    
    
