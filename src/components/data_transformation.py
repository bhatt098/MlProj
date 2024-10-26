import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pickle

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,Target_feature


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path= os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_tranformation_config = DataTransformationConfig()
        self.target_feature = Target_feature

    def get_data_transformation_object(self,numerical_features,categorical_features):
        try:
            logging.info('inside get_data_transformation_object method')
            numerical_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='median')),  # Impute missing values
                ('scaler', StandardScaler())  # Scale numerical features
            ])
            categorical_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='most_frequent')),  # Impute missing categorical values
                ('encoder', OneHotEncoder(drop='first'))  # Encode categorical features
            ])
            preprocessor = ColumnTransformer([
                ('numerical', numerical_pipeline, numerical_features),
                ('categorical', categorical_pipeline, categorical_features)
            ])
            # preprocessor = ColumnTransformer([
            #     ('missing_numerical_values',SimpleImputer(strategy='median'),numerical_features),
            #     ('missing_categorcial_values',SimpleImputer(strategy='most_frequent'),categorical_features),
            #     ('encoding',OneHotEncoder(drop='first'),categorical_features),
            #     ('scaling',StandardScaler(),numerical_features)
            # ])
            return preprocessor
        

        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_tranformation(self,train_path,test_path):
        try:
            logging.info('inside initiate_data_tranformation , Reading training and testing data')
            train_df=pd.read_csv(train_path,index_col=0)
            test_df=pd.read_csv(test_path,index_col=0)
            
            categorical_features=[feature for feature in train_df.columns if train_df[feature].dtypes=='O' ]
            numerical_features=[feature for feature in train_df.columns if train_df[feature].dtypes!='O' and feature!=self.target_feature]
            
            logging.info('calling get_data_transformation_object method')
            preprocessor_obj=self.get_data_transformation_object(numerical_features,categorical_features)
            
            X_train=train_df.drop(columns=[self.target_feature],axis=1)
            X_test=test_df.drop(columns=[self.target_feature],axis=1)
            
            y_train=train_df[self.target_feature]
            y_test=test_df[self.target_feature]
            
            logging.info('Doing fit_tranform on train dataset')
            X_train_array = preprocessor_obj.fit_transform(X_train)
            X_test_array = preprocessor_obj.transform(X_test)
            print(X_train_array)
            train_array=np.c_[X_train_array,np.array(y_train)]
            test_array=np.c_[X_test_array,np.array(y_test)]
            
            save_object(self.data_tranformation_config.preprocessor_obj_file_path,preprocessor_obj)
            
            return(
                train_array,
                test_array,
                self.data_tranformation_config.preprocessor_obj_file_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
        
        

