import os
import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import psycopg2
load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('dbname')
port = os.getenv('port')

def read_sql_data():
    logging.info("Reading Mysql database started")
    try:
        mydb = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            dbname = db,
            port = port
        )
        logging.info("Connection Established,{mydb}")
        df = pd.read_sql_query("Select * from student limit 1000",mydb)
        print(df.head())

        return df
    except Exception as e:
        raise CustomException(e,sys)


