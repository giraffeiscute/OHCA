"""
AED_deployment_model
Author: Kexin Cao
Institute: Tsinghua University
Date: 20241220 
"""

import Data
import ModelBuilder
from gurobipy import *
import random
import numpy as np
import pandas as pd
import csv

if __name__ == "__main__":
    
    file_name = 'test_poi_df_total.csv'
    file_name_ohca = 'ohca_df.csv'
    # loc_num = 5
    loc_num_list = [5, 10,20,40, 60, 80, 100]
    # loc_num_list = [5]
    dist_limit = 1.2
    build_num = 5000
    build_num_choose_cnt = 10
    build_sum = 99724
    ohca_cover_random_cnt = 10

    
    # df = pd.DataFrame(random_candidate_loc_id).T
    # output_name = 'build_num_choose_' + str(loc_num)+ '_set_' + str(cnt)
    # df.to_csv(output_name, index=False)   
    
    
        
    for loc_num in loc_num_list:  
        random_candidate_loc_id = np.zeros((build_num_choose_cnt, build_num))
                
        # for cnt in range(build_num_choose_cnt):
        #     random_candidate_loc_id[cnt]=random.choices(range(build_sum), k=build_num)
        # output_name = 'build_num_choose_' + str(loc_num)+ '_set_' + str(build_num_choose_cnt)
        # np.save(output_name,random_candidate_loc_id)   
        output_name = 'build_num_choose_' + str(loc_num)+ '_set_' + str(build_num_choose_cnt) + '.npy'
        random_candidate_loc_id = np.load(output_name).astype(np.int64)        
   
        data = Data.Data()
        # data.read_data(file_name,file_name_ohca,loc_num=loc_num,dist_limit=dist_limit,build_num=build_num)   
        data.read_npy(file_name,file_name_ohca,dist_limit=dist_limit,build_num=build_num)   
        print('read finishing !')
        
        random_choose_coverage = np.zeros((build_num_choose_cnt,ohca_cover_random_cnt))
        random_choose_survivalrate_average = np.zeros((build_num_choose_cnt,ohca_cover_random_cnt))    
        for cnt in range(build_num_choose_cnt):
            candidate_loc_id = random_candidate_loc_id[cnt]
            random_choose_loc_id = np.zeros((ohca_cover_random_cnt, loc_num))
            random_choose_survivalrate = np.zeros(len(data.ohca_lat))
            ohca_cover_cnt_random = {}
            for i in range(ohca_cover_random_cnt):
                random_choose_loc_id[i] = random.choices(candidate_loc_id, k=loc_num)
                ohca_cover_cnt_random[i] = 0
                for ohca in range(len(data.ohca_lat)):
                    iscover = 0
                    min_dist = np.inf
                    for id in range(len(random_choose_loc_id[i])):
                        loc = int(random_choose_loc_id[i][id])
                        dist_loc_ohca = data.haversine(data.loc_lat[loc],data.loc_lon[loc],data.ohca_lat[ohca],data.ohca_lon[ohca])
                        if dist_loc_ohca <= min_dist:
                            min_dist = dist_loc_ohca                        
                        if dist_loc_ohca <= dist_limit:
                            iscover = 1
                    t_loc_ohca = min_dist / 240
                    if t_loc_ohca <= 4:
                        s_loc_ohca = (1 + np.exp(-0.26 + 0.106 * t_loc_ohca + 0.139 * 10.5))**(-1)
                    else:
                        s_loc_ohca = 0  
                    random_choose_survivalrate[ohca] = s_loc_ohca      
                    if iscover == 1:
                        ohca_cover_cnt_random[i] += 1
                random_choose_coverage[cnt][i] = ohca_cover_cnt_random[i]
                random_choose_survivalrate_average[cnt][i]  = np.average(random_choose_survivalrate)
           
            # random_choose_coverage[cnt] = np.average(ohca_cover_cnt_random.values)
            

                
            # print('{} : {}'.format('ohca_cover_cnt_predict', ohca_cover_cnt_predict), end='')
            # print()
                # print('{} : {}'.format('ohca_cover_cnt_random', ohca_cover_cnt_random[i]), end='')
                # print()
            output_name = 'results/random_choose_loc_id_' + str(loc_num)+ '_set_' + str(cnt)
            np.save(output_name,random_choose_loc_id)
        output_name = 'results/random_choose_coverage_' + str(loc_num)+ '_set_' + str(build_num_choose_cnt)
        np.save(output_name,random_choose_coverage) 
        output_name = 'results/random_choose_survivalrate_average_' + str(loc_num)+ '_set_' + str(build_num_choose_cnt)
        np.save(output_name,random_choose_survivalrate_average)
                
        

