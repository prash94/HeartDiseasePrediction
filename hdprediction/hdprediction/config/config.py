import pathlib as pl

package_root = pl.Path(__file__).resolve().parent
model_dir = package_root / 'hdprediction'
datasets = package_root / 'data'


# define feature variables
# ADAPT: define target variable as required in the original model
target = 'cardio'
col_id = 'id'


final_feature_set = []