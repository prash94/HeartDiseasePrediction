"""
Load data
---------

"""

import pathlib
import pandas as pd
from hdprediction.hdprediction import config

def read_data_file(*, filename: str, sep: str):

    rawdata = pd.read_csv(f'{config.datasets}/{filename}', sep=sep)

    return rawdata
    # TODO: currently designed for csv files but needs to be expanded to json etc

# test = LoadRawData()
# # dt,featlog =test.read_data_file(file_name='cardio_train.csv',sep=";")
