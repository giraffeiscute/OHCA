English version underneath
# 公共自動體外心臟去顫器部署研究：結合 SHAP 可解釋分析的學習再優化方法
本專案為論文《Public Access Defibrillator Deployment for Cardiac Arrests: A Learn-Then-Optimize Approach with SHAP-based Interpretable Analytics》的實作代碼。我們提出一個創新的「先學習、後優化（Learn-Then-Optimize）」框架，結合地理資料機器學習模型、SHAP 可解釋性分析，以及整數規劃，解決院外心臟驟停（OHCA）風險預測與 AED（自動體外心臟去顫器）最適部署問題。

## 專案特色
### 多模型機器學習與跨區域泛化能力強化
本研究同時運用了多種機器學習方法，包括 XGBoost、Multilayer Perceptron（MLP）與支援向量機（SVM） 等，對 OHCA 風險進行建模與預測，以提升模型的穩定性與準確性。

### 無需人口統計資料，即可預測 OHCA 高風險區域\
模型僅使用 OpenStreetMap 的 POI 與建築分布資料作為輸入，測試集 R² 可達 0.75，證明地理資訊對於 OHCA 風險具有高度預測力。

### SHAP 可解釋性分析
利用 SHAP 模型量化各類建築（如住宅、公寓、診所等）對 OHCA 預測風險的貢獻，提供透明可解釋的依據協助公共衛生決策。

### 整數規劃 AED 部署優化模型
將 SHAP 權重轉化為空間風險密度，納入模型目標函數，考慮實際部署條件（如 AED 間距與覆蓋範圍），產出部署策略。

## 實驗成果亮點
1. 小規模部署下，相較隨機佈局，OHCA 覆蓋率提升最高達 49%

2. 大規模部署下（N = 100），平均病患存活率提升超過 16%

3. 敏感度分析顯示最佳 AED 間距為 1.2 公里，與實際黃金四分鐘反應時間相符

4. SHAP 分析揭示高住宅密度（如 apartment）與 OHCA 高發生率具有高度關聯

## 專案目錄說明
notebooks/：模型訓練、SHAP 分析與可視化

optimization/：AED 部署優化的整數規劃模型實作

## 引用方式
如果你在研究中使用本專案，請引用以下論文：

Yang, C.-Y., Leong, K.-H., Cao, K., Yang, M., & Chan, W. K. (2025). Public Access Defibrillator Deployment for Cardiac Arrests: A Learn-Then-Optimize Approach with SHAP-based Interpretable Analytics. arXiv preprint arXiv:2401.00682.




# Public Access Defibrillator Deployment for Cardiac Arrests: A Learn-Then-Optimize Approach with SHAP-based Interpretable Analytics
This repository contains the implementation of our paper "Public Access Defibrillator Deployment for Cardiac Arrests: A Learn-Then-Optimize Approach with SHAP-based Interpretable Analytics." We propose an innovative Learn-Then-Optimize framework that integrates geographic-data-based machine learning models, SHAP-based interpretability, and integer programming to address the prediction of out-of-hospital cardiac arrest (OHCA) risks and the optimal deployment of Automated External Defibrillators (AEDs).

## Project Highlights
### Multi-model Machine Learning and Cross-Region Generalization
We adopt multiple machine learning approaches—XGBoost, Multilayer Perceptron (MLP), and Support Vector Machine (SVM)—to model and predict OHCA risks, enhancing both the stability and accuracy of predictions.

### Predicting OHCA Hotspots Without Demographic Data
Our models rely solely on Point-of-Interest (POI) and building distribution data from OpenStreetMap as inputs. The neural network model achieves an R² over 0.75 on the test set, demonstrating that geographic features alone are highly informative for OHCA risk prediction.

### SHAP-Based Interpretability
We employ SHAP to quantify the contribution of different building and POI types (e.g., apartments, clinics) to OHCA risk. This enhances model transparency and provides explainable insights for public health decision-making.

### Integer Programming for AED Deployment Optimization
We transform SHAP-derived risk into spatial density scores and embed them in an integer programming model that accounts for real-world deployment constraints such as AED spacing and coverage radius.

## Key Experimental Findings
1. In small-scale deployment settings, our method outperforms random placement by up to 49% in OHCA coverage.

2. In large-scale deployments (N = 100), the average patient survival rate improves by over 16%.

3. Sensitivity analysis identifies the optimal AED spacing to be 1.2 km, aligning with the four-minute response window.

4. SHAP analysis confirms a strong correlation between residential density (e.g., apartments) and OHCA incidence.

## Project Structure
notebooks/: Model training, SHAP analysis, and visualization

optimization/: Integer programming implementation for AED deployment optimization

## Citation
If you use this repository in your research, please cite:

Yang, C.-Y., Leong, K.-H., Cao, K., Yang, M., & Chan, W. K. (2025). Public Access Defibrillator Deployment for Cardiac Arrests: A Learn-Then-Optimize Approach with SHAP-based Interpretable Analytics. arXiv preprint arXiv:2401.00682.
