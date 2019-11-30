# -*- coding: utf-8 -*-


__author__ = "zhouzhuofei"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.api import anova_lm
from statsmodels.formula.api import ols
import seaborn
seaborn.set()

purity = pd.Series([86.91, 89.85, 90.28, 86.34, 92.58, 87.33, 86.29, 91.86, 95.61, 89.86, 96.73, 99.42, 98.66, 96.07, 93.65, 87.31, 95.00, 96.85, 85.20, 90.56])
hydro = pd.Series([1.02,1.11,1.43,1.11,1.01,0.95,1.11,0.87,1.43,1.02,1.46,1.55,1.55,1.55,1.40,1.15,1.01,0.99,0.95,0.98])
data = pd.DataFrame({'purity': purity, 'hydro': hydro})
formula = 'purity ~ hydro'
lm = ols(formula, data).fit()
table = anova_lm(lm)
print(lm.summary())
print(table)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.scatter(data['hydro'], data['purity'], color='red', linewidth=1)
plt.plot(data['hydro'], lm.predict(data['hydro']), color='black', linewidth=1)
plt.title('氧气含量和烃的百分比')
plt.xlabel('hydro')
plt.ylabel('purity')
plt.show()


# answers:
# a: purity = 11.801 * hydro + 77.8633
# b: H_0: \beta = 0, H_1: \beta not = 0; t0=\beta/Se(\beta)=3.485, so H_1 right
# c: R^2 = 0.389
# d: [4.479, 19.123]
# e: hydro = 1.00 ; purity = 89.6643; [87.525, 91.803]

