# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:59:03 2024

@author: Yuan
"""

import statsmodels.api as sm
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

h3_l7_df = pd.read_json("h3_l7_df.json", orient="records", lines=True)
# 將 h3_l7_df 資料框中的 'id' 列移除，僅保留數據進行正規化
normalized_h3_l7_df = h3_l7_df.drop('id', axis=1)

# 對數據進行正規化：將每個數據列的最小值調整為 0，最大值調整為 1
normalized_h3_l7_df = (normalized_h3_l7_df - normalized_h3_l7_df.min()) / (normalized_h3_l7_df.max() - normalized_h3_l7_df.min())


X =  normalized_h3_l7_df.iloc[:,:-1]    # data without ID and OHCA
y =  normalized_h3_l7_df.iloc[:, -1]           # 標籤

# 增加常數項以包含截距
X = sm.add_constant(X)

# 建立線性回歸模型
mod = sm.OLS(y, X, missing='drop')
results = mod.fit()

#X內部相關性分析
correlation = X.corr()

sns.set(font_scale=1.5)

sns.set_context({"figure.figsize":(8,8)})
sns.heatmap(data = X, square = True, cmap="RdBu_r", annot = True)


# 輸出結果
print(results.summary())