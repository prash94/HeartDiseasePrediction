import pathlib

import pandas as pd


class LoadRawData:

    def read_data_file(self, file_name, sep=",", **path):
        if len(path) == 0:
            self.path_data = pathlib.Path.cwd().parent.joinpath('data')
        else:
            self.path_data = pathlib.Path(str(path['path']))
        self.rawdata = pd.read_csv(self.path_data.joinpath(file_name), sep=sep)
        print(f'file {file_name} read successfully with shape: {self.rawdata.shape}')
        return self.rawdata
