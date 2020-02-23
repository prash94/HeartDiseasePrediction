#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import pathlib as pl
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold


# In[ ]:


# TODO: make sure you have done test train split before feature selection


# In[2]:


# TODO: use datset as an input from a difference class instead of this
pth = pl.Path.cwd()
file_path = pth.joinpath('Downloads', 'cardiovascular-disease-dataset', 'cardio_train.csv')
dt = pd.read_csv(file_path, sep = ";")


# TODO: Automate determination of continuous variables in a different class and call it instead of manual definition
numerical_variables = dt[['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol']]


dt_Cont_Cols = {}
for i in range(len(dt_Cont.columns)):
    dt_Cont_Cols[str(i)] = dt_Cont.columns[i]


# In[3]:


dt.columns


# In[28]:


# TODO: call the dataexplorer.separatevariables() here to get these lists

continuous_variables = []
discrete_variables = []
col_list = list(dt.columns)
col_list.remove('id')
for var in col_list:
    if dt[var].nunique() >= 20:
        continuous_variables.append(var)
    else:
        discrete_variables.append(var)


# In[35]:


# separate dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(
    dt.drop(labels=['id'], axis=1),
    dt['id'],
    test_size=0.3,
    random_state=0)

X_train.shape, X_test.shape


# In[67]:


def remove_constant_features(ds_train, ds_test):
    varthr = VarianceThreshold(threshold=0)
    varthr.fit(ds_train)
    # get_support() gives the list of non-constant features
    contant_features = [var for var in ds_train.columns if var not in ds_train.columns[varthr.get_support()]]
    print(contant_features)
    ds_train = varthr.transform(ds_train)
    ds_test = varthr.transform(ds_test)
    
#     TODO: convert the above two arrays in to data frames
    print(type(ds_train))
#     TODO: update the log
    
    varthr_q = VarianceThreshold(threshold=0.01)
    varthr_q.fit(ds_train)
    quasi_contant_features = [var for var in ds_train.columns if var not in ds_train.columns[varthr_q.get_support()]]
    print(quasi_contant_features)
    return ds_train, ds_test


# In[68]:


remove_constant_features(X_train, X_test)


# In[ ]:




