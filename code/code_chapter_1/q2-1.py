# -*- coding: utf-8 -*-


__author__ = "zhouzhuofei"

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.api import anova_lm
import matplotlib.pyplot as plt
import numpy as np
import seaborn
import sys
import os
seaborn.set()

discfile = '~/answers-for-linear-regression-analysis/DataSets/Appendices/data-table-B1.xls'
data = pd.read_excel(discfile)
formula = 'y ~ x8'
lm = ols(formula, data).fit()
table = anova_lm(lm)
intercept = lm.params['Intercept']
k = lm.params['x8']
print('y = ',intercept,'+',k,'*x8')
print(lm.summary())
print(table)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.scatter(data['x8'], data['y'], alpha=0.8, linewidths=2, color="black")
plt.plot(data['x8'], lm.predict(data['x8']), color="blue", linewidth=1)
plt.xlabel("冲球码数")
plt.ylabel("胜场数")
plt.show()




