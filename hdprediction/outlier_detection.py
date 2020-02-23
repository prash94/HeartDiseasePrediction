#!/usr/bin/env python
# coding: utf-8

# In[418]:


import pandas as pd
import pathlib as pl
import numpy as np


# In[448]:


# TODO: use datset as an input from a difference class instead of this
pth = pl.Path.cwd()
file_path = pth.joinpath('Downloads', 'cardiovascular-disease-dataset', 'cardio_train.csv')
dt = pd.read_csv(file_path, sep = ";")


# TODO: Automate determination of continuous variables in a different class and call it instead of manual definition. Do this in data processing pipeline
dt_Cont = dt[['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol']]


dt_Cont_Cols = {}
for i in range(len(dt_Cont.columns)):
    dt_Cont_Cols[str(i)] = dt_Cont.columns[i]


# In[449]:


# as i could not establis these outliers are due to difference in units or data input errors, i'm deleting them
orig_rows = dt_Cont.shape[0]
dt_Cont.set_index('height')
dt_Cont = dt_Cont.drop(dt_Cont['height'][dt_Cont['height']<140].index, axis=0)
dt_Cont = dt_Cont.drop(dt_Cont['weight'][dt_Cont['weight'] < 50].index, axis=0)
dt_Cont = dt_Cont.drop(dt_Cont['ap_hi'][(dt_Cont['ap_hi'] < 60) | (dt_Cont['ap_hi'] > 300)].index, axis=0)
dt_Cont = dt_Cont.drop(dt_Cont[(dt_Cont['ap_lo'] < 40) | (dt_Cont['ap_lo'] > 150)].index, axis=0)
print(f'excluded {orig_rows-dt_Cont.shape[0]} rows as they seem abnormal values' )


# In[450]:


def measures_of_central_tendency():
    dict_measures_ct = {}
    for var in dt_Cont:
        dict_measures_ct[var] = {}
        std = dt_Cont[var].std()
        mean = dt_Cont[var].mean()
        quartile1, quartile4 = np.percentiles(dt_Cont[var], [75,25])
        dict_measures_ct[var]['std'] = std
        dict_measures_ct[var]['mean'] = mean
        dict_measures_ct[var]['quartile1'] = quartile1
        dict_measures_ct[var]['quartile4'] = quartile4
    return dict_measures_ct


# In[441]:


def outlierdetection():
    dt_Cont2 = dt_Cont.copy(deep=False)
    dict_cont_outliers = {}
    for var in dt_Cont_Cols.values():
        dict_cont_outliers[var] = {}
        
        dict_measures = measures_of_central_tendency()
        upper = dict_measures[var]['mean'] + 3*(dict_measures[var]['std'])
        lower = dict_measures[var]['mean'] - 3*(dict_measures[var]['std'])
        dt_Cont2[str(var)+'outlier_flag'] = (dt_Cont[var] > upper) | (dt_Cont[var] < lower)
        
        
        dict_cont_outliers[var]['totalrecords'] = dt_Cont2.shape[0]
        dict_cont_outliers[var]['mean'] = dict_measures[var]['mean'].max()
        dict_cont_outliers[var]['standard_Deviation'] = dict_measures[var]['std'].max()
        dict_cont_outliers[var]['outliers'] = dt_Cont2[str(var)+'outlier_flag'].sum()
        dict_cont_outliers[var]['%_outliers'] = dict_cont_outliers[var]['outliers']*100/ dict_cont_outliers[var]['totalrecords']
#     outlier_columns = [col for col in dt_Cont.columns if '_outlier_flag' in col]
    return pd.DataFrame(dict_cont_outliers)
#     return outlier_columns


# In[442]:


outlierdetection()
# pd.DataFrame(measures_of_central_tendency()).T


# In[ ]:


quartile1, quartile4 = 


# In[445]:


from sklearn.cluster import DBSCAN
# seed(1)
# random_data = np.random.randn(50000,2)  * 20 + 20

outlier_detection = DBSCAN(min_samples = 5, eps = 20)
clusters = outlier_detection.fit_predict(dt_Cont)
list(clusters).count(-1)


# In[446]:


dt_cont_clusters = pd.concat([dt_Cont,pd.DataFrame(clusters, index=dt_Cont.index)], axis=1)
# dt_cont_clusters.head()
# dt_cont_clusters[(dt_cont_clusters['weight'] >= 100) & (dt_cont_clusters[0] != -1)]
dt_cont_clusters[dt_cont_clusters[0] == -1].shape


# In[447]:


dt_cont_clusters[dt_cont_clusters[0] == -1]


# In[ ]:


# Inter quartile range


# In[ ]:


# record all of these along with original values into a data frame and visualise to see the patterns and then make a decision


# In[ ]:


# do normality checks once again

