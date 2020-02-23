import pathlib as pl
from sklearn.externals import joblib

# TODO: need to defile this object with actual pipeline
import pipeline

package_root = pl.Path(__file__).resolve().parent
model_dir = package_root / 'hdprediction'
datasets = package_root / 'data'

# ADAPT: define target variable as required in the original model
target = 'cardio'
col_id = 'id'

feature_list = ['id', 'age', 'gender', 'height',
                'weight', 'ap_hi', 'ap_lo', 'cholesterol',
                'gluc', 'smoke', 'alco', 'active', 'cardio']


def save_pipeline(*, pipeline_to_persist) -> None:
    """Persis the pipeline"""

    save_file_name = 'heart_disease_lr.pkl'
    save_path = model_dir / save_file_name
    joblib.dump(pipeline_to_persist, save_path)

    print('saved pipeline')

def run_training() -> None:
    """train the model"""

