"""
Load data
---------

"""

import pathlib
import pandas as pd


class LoadRawData(*, file_name: str) -> pd.DataFrame:


    def __init__(self):
        self.feature_prep_log = {}

    def read_data_file(*, file_name: str, sep: str, **path):
        self.feature_prep_log['load_data'] = {}
        if len(path) == 0:
            self.path_data = pathlib.Path.cwd().parent.joinpath('data')
        else:
            self.path_data = pathlib.Path(str(path['path']))

        self.rawdata = pd.read_csv(self.path_data.joinpath(file_name), sep=sep)

        # save output to a log
        self.feature_prep_log['load_data']['message'] = 'file read successfully'
        self.feature_prep_log['load_data']['output'] = 'rawdata'
        self.feature_prep_log['load_data']['output_type'] = 'file name & shape'

        print(f'file read successfully with shape: {self.rawdata.shape}')
        return self.rawdata, self.feature_prep_log
        # TODO: currently designed for csv files but needs to be expanded to json etc

# test = LoadRawData()
# # dt,featlog =test.read_data_file(file_name='cardio_train.csv',sep=";")
