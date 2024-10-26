from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd
import os


class PredictPipeline:
    def __init__(self):
        pass
    
    
    def predict(self,input_data):
        try:
            
            model_path=os.path.join('artifacts','model.pkl')
            preprocessed_path=os.path.join('artifacts','preprocessor.pkl')
            model=load_object(model_path)
            preprocesser=load_object(preprocessed_path)
            preprocessed_data=preprocesser.transform(input_data)
            return model.predict(preprocessed_data)
        
        except Exception as e:
            raise CustomException(e,sys)
        


class CustomData:
    """"
      CustomData Class aims to take inputs and return 
      DataFrames...
    """
    def __init__(self,gender:str,race_ethnicity:str,parental_level_of_education:str,lunch:str,test_preparation_course:str,
                 reading_score:int,writing_score:int
                 ):
        
        self.gender=gender,
        self.race_ethnicity=race_ethnicity,
        self.parental_level_of_education=parental_level_of_education,
        self.lunch=lunch,
        self.test_preparation_course=test_preparation_course,
        # self.math_score=math_score,
        self.reading_score=reading_score,
        self.writing_score=writing_score
        
    def get_data_as_dataframe(self):
        try:
            input_dict={
                'gender':self.gender,
                'race_ethnicity':self.race_ethnicity,
                'parental_level_of_education':self.parental_level_of_education,
                'lunch':self.lunch,
                'test_preparation_course':self.test_preparation_course,
                # 'math_score':self.math_score,
                'reading_score':self.reading_score,
                'writing_score':self.writing_score
            }
            return pd.DataFrame(input_dict)
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
        


# if __name__=="__main__":
#     obj=DataIngestion()
#     train_path,test_path = obj.initiate_data_ingestion()
#     obj1=DataTransformation()
#     train_array,test_array,preprocessed_obj=obj1.initiate_data_tranformation(train_path,test_path)
#     obj2=ModelTrainer()
#     obj2.initiate_model_trainer(train_array,test_array,preprocessed_obj)