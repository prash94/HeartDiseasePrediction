import pipeline
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

from hdprediction.dataextraction import read_data_file
from hdprediction.hdprediction import config

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

#     load data
    data = read_data_file(filename=config.training_data_file)

    x_train, x_test, y_train,y_test = train_test_split(
        data[config.final_feature_set],
        data[config.target],
        test_size = 0.25,
        random_state=0)

    pipeline.