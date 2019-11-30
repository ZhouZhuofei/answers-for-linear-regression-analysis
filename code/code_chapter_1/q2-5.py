# -*- coding: utf-8 -*-


__author__ = "zhouzhuofei"
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.api import anova_lm
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

discfile = '~/answers-for-linear-regression-analysis/DataSets/Appendices/data-table-B3.xls'
data = pd.read_excel(discfile)
formula = 'y ~ x10'
lm = ols(formula, data).fit()
table = anova_lm(lm)
print(lm.summary())
print(table)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.scatter(data['x10'], data['y'], alpha=0.8, linewidth=2, color='red')
plt.plot(data['x10'], lm.predict(data['x10']), color='blue', linewidth=1)
plt.ylabel("燃油效率/(ft/gal)")
plt.xlabel("车重")
plt.title('拟合线和散点图')
plt.show()


