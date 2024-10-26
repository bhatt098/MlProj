import os
import sys
import pickle
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


Target_feature='math_score'

def save_object(file_path,object):
    """"
       getting used to save data as a pickle file 
       method expects file path and object.
    """
    try:
        logging.info('inside save_object method')
        
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as f:
            pickle.dump(object,f)
            
    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as f:
            obj=pickle.load(f)
        return obj
    except Exception as e:
        raise CustomException(e,sys)


def evaluate_model(X_train,X_test,y_train,y_test,models,params):
    try:
        report = {}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            print(list(models.keys())[i])
            print(model)
            param=params[list(models.keys())[i]]
            gs= GridSearchCV(model,param,cv=3)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)

            
            # print(X_train)
            model.fit(X_train,y_train)
            y_pred=model.predict(X_test)
            model_score = r2_score(y_test,y_pred)
            
            report[list(models.keys())[i]]=model_score
        
        # for model in models.values():
        #     model.fit(X_train,y_train)
        #     y_pred=model.predict(X_test)
        #     model_score = r2_score(y_test,y_pred)
            
        #     report[model]=model_score            
        return report
            
    except Exception as e:
        raise CustomException(e,sys)
        
        
    