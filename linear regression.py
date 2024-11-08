# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:14:45 2024

@author: Yuan
"""





import pandas as pd
import numpy as np
import random
import statsmodels.api as sm

h3_l7_df = pd.read_json("h3_l7_df.json", orient="records", lines=True)



# 設定訓練、驗證和測試集的比例
train_proportion = 0.7   

# 將 h3_l7_df 資料框中的 'id' 列移除，僅保留數據進行正規化
normalized_h3_l7_df = h3_l7_df.drop('id', axis=1)

# 對數據進行正規化：將每個數據列的最小值調整為 0，最大值調整為 1
normalized_h3_l7_df = (normalized_h3_l7_df - normalized_h3_l7_df.min()) / (normalized_h3_l7_df.max() - normalized_h3_l7_df.min())

# 設定隨機種子並打亂數據
seed = 77
np.random.seed(seed)
random.seed(seed)

# 將數據轉換成 numpy array 並打亂
h3_l7_id = np.random.choice(normalized_h3_l7_df.shape[0], normalized_h3_l7_df.shape[0], replace=False)
spatial_data = normalized_h3_l7_df.iloc[h3_l7_id].to_numpy()

# 分割訓練和測試數據集
train_size = int(spatial_data.shape[0] * train_proportion)
train_spatial_data = spatial_data[:train_size, :]
test_spatial_data = spatial_data[train_size:, :]

# 分離特徵和標籤
X_train = train_spatial_data[:, :-1]   # features
y_train = train_spatial_data[:, -1]    # target
X_test = test_spatial_data[:, :-1]
y_test = test_spatial_data[:, -1]

# 增加常數項以包含截距
X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)

# 建立線性回歸模型
mod = sm.OLS(y_train, X_train, missing='drop')
res = mod.fit()

# 輸出結果
print("訓練結果：")
print(res.summary())