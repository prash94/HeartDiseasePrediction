import pandas as pd
from hdprediction.dataextraction import LoadRawData as ld_read
from sklearn.base import BaseEstimator, TransformerMixin


class DataExplore():

    def __init__(self)->None:

        self.feature_sets_dict = {}

        # self.categorical_variables = []
        # self.numerical_variables = []
        # self.numerical_missing_values = []
        # self.discrete_variables = []
        # self.dichotomous_variables = []
        # self.cat_lable_count = {}
        # self.ld_read = LoadRawData()
        self.raw_data, \
        self.feature_prep_log = self.ld_read.read_data_file\
            (file_name='cardio_train.csv',sep=";")

    def separatevariables(self,id,**discrete_limit):
        # exclude id
        self.raw_data = self.raw_data.drop(columns=id)

        # List of categorical variables
        self.feature_sets_dict['categorical_variables'] = [var for var in self.raw_data.columns
                                      if self.raw_data[var].dtypes == 'O']
        #
        self.feature_prep_log['categorical_variables']['message'] = f'There are ' \
            f'{len(self.categorical_variables)} ' \
            f'categorical variables ' \
            f'in the dataset'
        # self.feature_prep_log['categorical_variables']['output'] = self.categorical_variables
        # self.feature_prep_log['categorical_variables']['output_type'] = 'list'


        # list of numerical variables
        self.numerical_variables = [var for var in self.raw_data.columns
                                    if self.raw_data[var].dtypes == 'int64'
                                    ]

        self.feature_prep_log['numerical_variables']['message'] = f'There are ' \
            f'{len(self.numerical_variables)} ' \
            f'numerical variables ' \
            f'in the dataset'
        self.feature_prep_log['numerical_variables']['output'] = self.numerical_variables
        self.feature_prep_log['numerical_variables']['output_type'] = 'list'

        # TODO:add this to missing values
        # self.numerical_missing_values = (self.raw_data.isna().sum() /
        #                                  self.raw_data.shape[0]).to_dict()

        # list of discrete variables
        self.discrete_variables = [var for var in self.numerical_variables if
                                   (self.raw_data[var].nunique(dropna=True) > 2) & (
                                           self.raw_data[var].nunique(dropna=True) < 20)]

        self.feature_prep_log['discrete_variables']['message'] = f'There are ' \
            f'{len(self.discrete_variables)} ' \
            f'discrete variables ' \
            f'in the dataset'
        self.feature_prep_log['discrete_variables']['output'] = self.discrete_variables
        self.feature_prep_log['discrete_variables']['output_type'] = 'list'

        # list of dichotomous variables
        self.dichotomous_variables = [var for var in self.numerical_variables if
                                      self.raw_data[var].nunique(dropna=True) == 2]

        self.feature_prep_log['dichotomous_variables']['message'] = f'There are ' \
            f'{len(self.dichotomous_variables)} ' \
            f'dichotomous variables ' \
            f'in the dataset'
        self.feature_prep_log['dichotomous_variables']['output'] = self.dichotomous_variables
        self.feature_prep_log['dichotomous_variables']['output_type'] = 'list'

        """
        if len(self.categorical_variables) == 0:
            print(f'There are no categorical variables in the dataset\n')
        else:
            print(f'There are {len(self.categorical_variables)} categorical variables in the dataset\n')
            print('list of categorical variables', self.categorical_variables)
        print(f'list of categorical variables: {self.cat_var}')

        if len(self.numerical_variables) == 0:
            print(f'There are no numerical variables in the dataset\n')
        else:
            print(f'There are {len(self.numerical_variables)} numerical variables in the dataset\n')
            print('list of numerical variables', self.numerical_variables)

        print(f'variables and their % of missing values: {self.numerical_missing_values}\n')
        print(f'list of discrete variables: {self.discrete_variables} \n')
        print(f'list of dichotomous variables: {self.dichotomous_variables}\n')
        """

        return self.discrete_variables, \
               self.dichotomous_variables, \
               self.numerical_variables, \
               self.numerical_missing_values, \
               self.categorical_variables, \
               self.cat_var, \
               self.feature_prep_log

    # no rows, columns,count by lable for cat, discrete and dichotomous vars, mean, sd, range, quartiles
    def describevariables(self):

        dict_measures_ct = {}
        cat_vars =
        # TODO: not tested with real example
        # TODO: add this to feature selection 1
        self.cat_lable_count = [var for var in self.categorical_variables if
                        (self.raw_data.groupby([var])['id'].count() /
                         len(self.raw_data['id'])).min() <= 0.05
                        ]
        return self.categorical_variables
        # for var in dt_Cont:
        #     dict_measures_ct[var] = {}
        #     std = dt_Cont[var].std()
        #     mean = dt_Cont[var].mean()
        #     quartile1, quartile4 = np.percentiles(dt_Cont[var], [75, 25])
        #     dict_measures_ct[var]['std'] = std
        #     dict_measures_ct[var]['mean'] = mean
        #     dict_measures_ct[var]['quartile1'] = quartile1
        #     dict_measures_ct[var]['quartile4'] = quartile4
        # return dict_measures_ct

    def negativevaluecheck(self):
        col_list = list(data_set.columns)
        if 'id' in col_list:
            col_list.remove('id')
    
        cols_neg_values = [col for col in col_list if data_set[col].min() < 0]

        if len(cols_neg_values) == 0:
            print('\nNegative value test: No negative values found')
        else:
            print('\ncheck for negative values in the following columns. Are they expected?\n\n',cols_neg_values)

        return cols_neg_values

    def missing_value_columns(self):
        col_list = list(data_set.columns)
        if 'id' in col_list:
            col_list.remove('id')

        cols_missing_values = [col for col in col_list if data_set[col].isnull().sum() > 0]

        if len(cols_missing_values) == 0:
            print('Missing value test: OK')
        else:
            print('check for missing values in the following columns\n', cols_missing_values)
        #     TODO: create a dict instead and add the % of missing values. \
        #           This can be used to set a threshold for which you need you need to impute
        return cols_missing_values


VarExp = DataExplorer()
VarExp.describevariables()
print('check:',VarExp.categorical_variables)
# def group_rare_lables(self, *,)
# def numerical_variables(self, *,:
#     variables and their distribution markers
#
