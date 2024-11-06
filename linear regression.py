# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:14:45 2024

@author: Yuan
"""




import json
import pandas as pd
import numpy as np
import json
import random

h3_l7_df = pd.read_json("h3_l7_df.json", orient="records", lines=True)
import statsmodels.api as sm


train_size = int(spatial_data.shape[0]*0.7)

seed = 77
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)

h3_l7_id = np.random.choice(spatial_data.shape[0], spatial_data.shape[0])
spatial_data = spatial_data[h3_l7_id]
train_spatial_data = spatial_data[:train_size, :]
test_spatial_data = spatial_data[train_size:, :]

X =  h3_l7_df.iloc[:, 1:52]    # data without ID and OHCA
y =  h3_l7_df.iloc[:, -1]           # 標籤


# 增加常數項以包含截距
X = sm.add_constant(X)

# 建立線性回歸模型
mod = sm.OLS(y, X, missing='drop')
res = mod.fit()
print("passs")
# 輸出結果
print(res.summary())