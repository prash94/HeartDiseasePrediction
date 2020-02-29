import pipeline
from sklearn.externals import joblib





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

