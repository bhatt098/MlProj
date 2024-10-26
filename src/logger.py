import logging
import os
# from datetime import datetime
import datetime

log_file=f"{datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(log_path,exist_ok=True)
log_file_path=os.path.join(log_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format="%(asctime)s %(lineno)d %(message)s",
    level=logging.INFO

)

# if __name__=="__main__":
#     logging.info('loggin has started')
#     print('completed')
