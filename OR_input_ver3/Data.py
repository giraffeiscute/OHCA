"""
AED_deployment_model
Author: Kexin Cao
Institute: Tsinghua University
Date: 20241220 
"""

import ModelBuilder
import pandas as pd
import math
import numpy as np

class Data(object):
    def __init__(self):
        self.loc_lat = None
        self.loc_lon = None
        self.loc_score = None
        
        self.dist_i_j = {}
        self.indicator_i_j = {}
        
        self.build_num = 0
        self.loc_num = 0
        self.dist_limit = 0
    
    def read_npy(self, file_name, file_name_ohca, dist_limit, build_num):
        # self.loc_num = loc_num
        self.dist_limit = dist_limit
        self.build_num = build_num
        self.file_name_ohca = file_name_ohca

        self.loc_lat = pd.read_csv(file_name, usecols = ['lat']).values
        self.loc_lon = pd.read_csv(file_name, usecols = ['lon']).values        
        self.loc_score = pd.read_csv(file_name, usecols = ['total_score']).values        
        self.ohca_lat = pd.read_csv(file_name_ohca, usecols = ['Latitude']).values
        self.ohca_lon = pd.read_csv(file_name_ohca, usecols = ['Longitude']).values
        

        self.indicator_i_j = np.load('indicator_i_j.npy')
        
    def read_data(self, file_name, file_name_ohca, loc_num, dist_limit, build_num):
        self.loc_num = loc_num
        self.dist_limit = dist_limit
        self.build_num = build_num
        self.file_name_ohca = file_name_ohca
        
        """ read_excel """
        self.loc_lat = pd.read_csv(file_name, usecols = ['lat']).values
        self.loc_lon = pd.read_csv(file_name, usecols = ['lon']).values
        self.loc_score = pd.read_csv(file_name, usecols = ['score']).values
        self.ohca_lat = pd.read_csv(file_name_ohca, usecols = ['Latitude']).values
        self.ohca_lon = pd.read_csv(file_name_ohca, usecols = ['Longitude']).values
        
        """ calculate dist """
        for i in range(self.build_num):
            for j in range(self.build_num):
                if i != j:
                    self.dist_i_j[i,j] = self.haversine(self.loc_lat[i],self.loc_lon[i],self.loc_lat[j],self.loc_lon[j]) 
                    if self.dist_i_j[i,j] <= self.dist_limit:
                        self.indicator_i_j[i,j] = 0
                    else:
                        self.indicator_i_j[i,j] = 1
    
    def haversine(self, lat1, lon1, lat2, lon2):
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
                    
                    
                    
                    
                    
                    