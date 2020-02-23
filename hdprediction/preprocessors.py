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
            
            
# fit and transform methods are needed to use sklearn pipeline
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
    
# this class is for encoding catagorical varialbles with a sequential number based on the mean target value per lable within the variable.
# Higher the mean more important the lable is. 
# TODO: Need to check if this works for classification models
class CategoricalEncoder(BaseEstimator, TransformerMixin):
    
    def __init__(self, variable_list=None):
        if not isinstance()
    
        
    

