from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer



if __name__=="__main__":
    obj=DataIngestion()
    train_path,test_path = obj.initiate_data_ingestion()
    obj1=DataTransformation()
    train_array,test_array,preprocessed_obj=obj1.initiate_data_tranformation(train_path,test_path)
    obj2=ModelTrainer()
    obj2.initiate_model_trainer(train_array,test_array,preprocessed_obj)