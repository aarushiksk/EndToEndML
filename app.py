from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components .data_ingestion import DataIngestion
from src.mlproject.components .data_ingestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        data_ingestion=DataIngestion()  #Creating an object of DataIngestion class
        data_ingestion.initiate_data_ingestion() #Calling the method of DataIngestion class
        
    except Exception as e:
        logging.error("Error occured")
        raise CustomException(e,sys)
    