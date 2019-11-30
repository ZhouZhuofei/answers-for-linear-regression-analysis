# -*- coding: utf-8 -*-


__author__ = "zhouzhuofei"
import pandas as pd
import numpy as np
from statsmodels.stats.api import anova_lm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

discfile = '~/answers-for-linear-regression-analysis/DataSets/Appendices/data-table-B4.xls'
data = pd.read_excel(discfile)
formula = 'y ~ x1'
lm = ols(formula, data).fit()
table = anova_lm(lm)
print(lm.summary())
print(table)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.scatter(data['x1'], data['y'], alpha=0.8, linewidth=1.0, color='blue')
plt.plot(data['x1'], lm.predict(data['x1']), color='black', linewidth=1.5)
plt.title("房屋销售价格和本期税额的关系")
plt.xlabel("本期税额/1000$")
plt.ylabel("房屋出售价格/1000$")
plt.show()




# answer:
# a: y = 3.32*x1 + 13.32
# b: see print(table)
# c: R^2 = 76.7%
# d: Se(beta) = 0.39;\hat{\beta} = [3.32 - 0.39*2.074, 3.32 + 0.39*2.704]
# e: when x = 750/1000 = 0.75, y_x1 = 3.32 * 0.75 + 13.32 = 15.81;E(y|x1) = [11.064, 20.556]

