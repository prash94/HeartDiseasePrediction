#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
# from lrmodel.processing.errors import InvalidModelInputError


# In[ ]:


# catagorical variables are imputed by labling them as 'Missing'
class ImputeCategoricalVariables(BaseEstimator, TransformerMixin):

    
    def __init__(self, variable_list=None) -> None:
        if not isinstance(variable_list, list):
            self.variable_list = [variable_list]
        else:
            self.variable_list = variable_list
            
            
# fit and transform methods are needed for using sklearn pipeline
    def fit(self, X:pd.DataFrame, y:pd.Series = None) -> 'ImputeCategoricalVariables':
        return self
    
    
    def transform(self, X:pd.DataFrame)
        X = X.copy()
        
        for feature in self.variable_list:
            X[feature] = X[feature].fillna('Missing')
            
        return X
    
# Numerical variable are imputed using mode
class ImputeNumericalVariables(BaseEstimator, TransformerMixin):
    
    
    def __init__(self, variable_list=None):
        if not isinstance(variable_list, list):
            self.variable_list = [variable_list]
        else:
            self.variable_list = variable_list
            
    
    def fit(self, X, y=None)
        self.imputer_metrc_dict = {}
        
        for feature in self.variable_list:
            self.imputer_metrc_dict[feature] = X[feature].mode()[0]
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variable_list:
            X[feature].fillna(self.imputer_metrc_dict, inplace=True)
        return X
            

# this class is for encoding catagorical variables if they are rarely occuring
# rarity is determined is using the tolerance
class RareLableCategoricalEncoder(BaseEstimator, TransformerMixin):
    
    
    def __init__(self, tol = 0.5, variable_list=None):
        self.tol = tol
        
        if not isinstance(variable_list, list):
            self.variable_list = [variable_list]
        else:
            self.variable_list = variable_list
            
    def fit(self, X, y=None):
        self.freq_lable_dict = {}
        
        for feature in self.variable_list:
            t = pd.Series(X[feature].value.counts()/np.float(len(X)))
            self.freq_lable_dict[feature] = list(t[t >= self.tol].index)
            
        return self
    
    def transform(self, X):
        X = X.copy()
        
        for feature in self.variable_list:
            X[feature] = np.where(X[feature].isin(self.freq_lable_dict[feature]), X[feature],'Rare')
            
        return X

class NegativeValueRemover(BaseEstimator, TransformerMixin):

    def __init__(self, variable_list=None):
        if not isinstance(variable_list, list):
            self.variable_list = [variable_list]
        else:
            self.variable_list = variable_list

    def fit(self, X:pd.DataFrame, y=None) -> 'NegativeValueRemover':
        return self

    def transform(self, x:pd.DataFrame) -> pd.DataFrame:
        x = x.copy()

        for col in self.variable_list:
            x = x.drop(x[x[col] < 0].index, inplace=True)
        return x

# this class is for encoding catagorical varialbles with a sequential number based on the mean target value per lable within the variable.
# Higher the mean more important the lable is. 
# TODO: Need to check if this works for classification models
class CategoricalEncoder(BaseEstimator, TransformerMixin):
    
    def __init__(self, variable_list=None):
        if not isinstance(variable_list, list):
            self.variable_list = [variable_list]
        else:
            self.variable_list = variable_list

    def fit(self, X, y):
        temp = pd.concat([X,y], axis=1)
        temp.columns = list(X.columns) + ['target']

#         persist transforming dictionary
        self.encoder_dict = {}

        for var in self.variable_list:
            t = temp.groupby([var])['target'].mean().sort_values(ascending=True).index
            self.encoder_dict[var] = {k: i for i, k in enumerate(t,0)}

        return self

    def transform(self, X):
        # TODO: Add the following code to all preprocessor methods
        # QUESTION: why de we need to create a copy?
        X = X.copy()
        for feature in self.variable_list:
            X[feature] = X[feature].map(self.encoder_dict[feature])

#        Check if this generates null values
        # QUESTION: what does any().any() do?
        if X[self.variable_list].isnull().any().any():
            null_counts = X[self.variable_list].isnull().any()
            vars = {key: value for (key, value) in null_counts.items() if value is True}

            raise InvalidModelInputError(
                f'Categorical encoder has introduced null values when'
                f'transforming categorical variables: {vars.keys()}'
            )
        return X


class feature_scaling(BaseEstimator, TransformerMixin):

    def scale_numerical_features(xtrain, xtest):
        xtrain_cont = xtrain[continuous_variables + discrete_variables]
        xtest_cont = xtest[continuous_variables + discrete_variables]
        xtrain_non_cont = xtrain.drop(continuous_variables + discrete_variables, axis=1)
        xtest_non_cont = xtest.drop(continuous_variables + discrete_variables, axis=1)

        scaler = MinMaxScaler()
        xtrain_scaled = scaler.fit_transform(xtrain_cont)
        xtest_scaled = scaler.transform(xtest_cont)

        xtrain_scaled = pd.DataFrame(xtrain_scaled, columns=xtrain_cont.columns, index=xtrain_cont.index)
        xtest_scaled = pd.DataFrame(xtest_scaled, columns=xtest_cont.columns, index=xtest_cont.index)

        x_train_ds = pd.concat([xtrain_non_cont, xtrain_scaled], axis=1)
        x_test_ds = pd.concat([xtest_non_cont, xtest_scaled], axis=1)

        print('x_train:', x_train_ds.shape)
        print('x_test:', x_test_ds.shape)

        return x_train_ds, x_test_ds

    x_train, x_test = scale_numerical_features(x_train, x_test)

