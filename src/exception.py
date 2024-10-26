import sys
from src.logger import logging

def error_message_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured at [{0}] line number {1} error message {2}".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message
  

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)                    # calling base class constructor
        self.error_message=error_message_details(error_message,error_details=error_details)

    def __str__(self):  # when we will print instance of the class it will print str return data
        return self.error_message

# if __name__=="__main__":
#     try:
#         a=1/0
#         print(a)
#     except Exception as e:
#         logging.info('an error has been occured')
#         raise CustomException(e,sys)

