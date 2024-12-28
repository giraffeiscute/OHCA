"""
AED_deployment_model
Author: Kexin Cao
Institute: Tsinghua University
Date: 20241220 
"""
import pandas as pd
import math


file_name = 'test_poi_df.csv'
# file_name_ohca = 'ohca_df.csv'
output_file_name = 'output.xlsx'
loc_num = 2
dist_limit = 0.96
build_num = 1000

loc_lat = pd.read_csv(file_name, usecols = ['lat']).values
loc_lon = pd.read_csv(file_name, usecols = ['lon']).values
# loc_score = pd.read_csv(file_name, usecols = ['score']).values
# ohca_lat = pd.read_csv(file_name_ohca, usecols = ['Latitude']).values
# ohca_lon = pd.read_csv(file_name_ohca, usecols = ['Longitude']).values

def haversine(lat1, lon1, lat2, lon2):
    # 将角度转换为弧度
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine公式
    d_lat = lat2 - lat1
    d_lon = lon2 - lon1
    a = math.sin(d_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    # 地球半径（单位：公里）
    r = 6371
    return c * r 

dist_i_j = {}
indicator_i_j = {}
""" calculate dist """
for i in range(build_num):
    for j in range(build_num):
        if i != j:
            dist_i_j[i,j] = haversine(loc_lat[i],loc_lon[i],loc_lat[j],loc_lon[j]) 
            if dist_i_j[i,j] <= dist_limit:
                indicator_i_j[i,j] = 0
            else:
                indicator_i_j[i,j] = 1

with pd.ExcelWriter(output_file_name, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
    pd.DataFrame(indicator_i_j.values).to_excel(writer, sheet_name = 'indicator', startcol=0)
    pd.DataFrame(dist_i_j.values).to_excel(writer, sheet_name = 'dist', startcol=0)

    

