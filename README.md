🧠 Public Access Defibrillator Deployment for Cardiac Arrests
🧠 公共自動體外心臟去顫器部署研究
This repository contains the implementation of our paper "Public Access Defibrillator Deployment for Cardiac Arrests: A Learn-Then-Optimize Approach with SHAP-based Interpretable Analytics."
本倉庫對應我們的論文《公共自動體外心臟去顫器部署研究：結合 SHAP 可解釋分析的學習再優化方法》的完整實作。

We propose a novel learn-then-optimize framework combining machine learning, SHAP-based interpretation, and integer programming to identify high-risk areas of out-of-hospital cardiac arrest (OHCA) and optimize AED (automated external defibrillator) placement accordingly.
我們提出一個創新的「先學習再優化」框架，結合機器學習、SHAP 可解釋模型分析以及整數規劃，來識別院外心臟驟停（OHCA）的高風險區域，並據此優化 AED（自動體外心臟去顫器）的部署策略。

🔍 Key Features
🔍 主要特點
ML-powered OHCA prediction using geographic data only: The model achieves over 0.75 R² on the test set using just POI and building features from OpenStreetMap.

僅使用地理資料的 OHCA 預測模型：模型僅利用來自 OpenStreetMap 的 POI 與建築資訊，即可在測試集上達到超過 0.75 的 R²。

SHAP-based interpretability: SHAP values quantify how each type of location (e.g., apartments, clinics) contributes to OHCA risk, enabling transparent decision-making.

基於 SHAP 的模型可解釋性：SHAP 值可量化不同類型地點（如住宅、公寓、診所）對 OHCA 風險的貢獻，提升決策透明度。

Integer programming optimization: A SHAP-weighted objective function helps determine the most effective AED deployment under real-world constraints like coverage radius and spacing.

整數規劃優化：透過 SHAP 加權目標函數，我們在如 AED 覆蓋範圍與最小間距等現實條件下，計算最有效的部署方案。

🧪 Experimental Highlights
🧪 實驗亮點
+49% OHCA coverage improvement over random deployment with small-scale setups.

小規模部署下，相較隨機佈局，OHCA 覆蓋率提升達 49%。

+16% improvement in average survival rate at full deployment scale (N=100).

在部署 100 台 AED 的情境下，平均存活率提升超過 16%。

Sensitivity analysis provides deployment guidelines for spacing and quantity.

敏感度分析提供 AED 間距與數量的佈局指引。

📁 Repository Structure
📁 倉庫結構
notebooks/: Model training, SHAP analysis, and visualizations

notebooks/：模型訓練、SHAP 解釋與可視化

optimization/: SHAP-guided integer programming for AED placement

optimization/：導入 SHAP 權重的 AED 整數規劃優化

data/: Instructions for accessing or generating geographic and OHCA data

data/：地理與 OHCA 數據取得或合成的說明

results/: Experimental results and deployment maps

results/：實驗結果與部署地圖
