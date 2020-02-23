#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import pathlib as pl
import numpy as np


# In[27]:


# TODO: use datset as an input from a difference class instead of this
pth = pl.Path.cwd()
file_path = pth.joinpath('Downloads', 'cardiovascular-disease-dataset', 'cardio_train.csv')
dt = pd.read_csv(file_path, sep = ";")


# TODO: Automate determination of continuous variables in a different class and call it instead of manual definition
dt_Cont = dt[['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol']]


dt_Cont_Cols = {}
for i in range(len(dt_Cont.columns)):
    dt_Cont_Cols[str(i)] = dt_Cont.columns[i]


# In[30]:


from  matplotlib import pyplot as plt
import math

fig, ax = plt.subplots(figsize=(8,4),ncols = 3,nrows=2, sharey = True,constrained_layout=False)
ax = ax.flatten()
# ax.plot()
# ax.plot(nrows = 3,ncols = math.ceil(len(dt_Cont.columns)/3))
# ax[0].hist(dt_Cont['age'], bins=20)
for key,value in dt_Cont_Cols.items():
    ax[int(key)].hist(dt_Cont[value])
    plt.autoscale
plt.show()


# In[7]:


from  statsmodels.graphics.gofplots import qqplot
import math

# fig, ax = plt.subplots(figsize=(8,4),ncols = 3,nrows=2, sharey = True,constrained_layout=False)
# ax = ax.flatten()
# ax.plot()
# ax.plot(nrows = 3,ncols = math.ceil(len(dt_Cont.columns)/3))
# ax[0].hist(dt_Cont['age'], bins=20)
for key,value in dt_Cont_Cols.items():
#     ax[int(key)].hist(dt_Cont[value])
    qqplot(dt_Cont[value], line='s')
    plt.autoscale
plt.show()


# In[8]:


# from  matplotlib import pyplot as plt
# import numpy as np
# from matplotlib import colors
# from matplotlib.ticker import PercentFormatter

# N_points = 100000
# n_bins = 20

# # Generate a normal distribution, center at x=0 and y=5
# x = np.random.randn(N_points)
# y = .4 * x + np.random.randn(100000) + 5

# fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# # We can set the number of bins with the `bins` kwarg
# axs[0].hist(x, bins=n_bins)
# axs[1].hist(y, bins=n_bins)


# In[9]:


import scipy
from numpy.random import seed

from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson
seed(1)
alpha = 0.05

def stats_normality(dataset=None, stats= []):
    dict_norm_stats = {}
    if shapiro in stats:
        for key,value in dt_Cont_Cols.items():
            dict_norm_stats[value] = {}
            shapiro_stat, shapiro_p = shapiro(dt_Cont[value])

            # interpret
            if shapiro_p > alpha:
                dict_norm_stats[value]['shapiro'] = 1
            else:
                dict_norm_stats[value]['shapiro'] = 0
    
    if normaltest in stats:
        for key,value in dt_Cont_Cols.items():        
            skewkurt_stat, skewkurt_p = normaltest(dt_Cont[value])
            
            # interpret
            if skewkurt_p > alpha:
                dict_norm_stats[value]['normaltest'] = 1
            else:
                dict_norm_stats[value]['normaltest'] = 0

    if anderson in stats:
        for key,value in dt_Cont_Cols.items(): 
            # normality test
            result = anderson(dt_Cont[value])
            p = 0
            for i in range(len(result.critical_values)):
                sl, cv = result.significance_level[i], result.critical_values[i]
                if result.statistic < result.critical_values[i]:
                    dict_norm_stats[value]['anderson'] = 1
                else:
                    dict_norm_stats[value]['anderson'] = 0
    return dict_norm_stats


# In[25]:


for key, value in dt_Cont_Cols.items():
    dt_Cont[value] = np.log(dt_Cont[value].abs())


# In[12]:


stats_normality(dataset=dt_Cont, stats= [shapiro,normaltest,anderson])


# In[29]:


for var in dt_Cont.columns:
    print(f'{var}: {max(dt_Cont[var])}')
    print(f'{var}: {min(abs(dt_Cont[var]))}')


# In[ ]:




