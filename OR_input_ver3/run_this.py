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
    # loc_num_list = [5,10,20,40,60,80,100]
    loc_num_list = [5]
    dist_limit = 0.96
    build_num = 5000
    build_num_choose_cnt = 10
    build_sum = 99724
    ohca_cover_random_cnt = 10
    

    # random_candidate_loc_id = []
    # for cnt in range(build_num_choose_cnt):
    #     random_candidate_loc_id.append(random.choices(range(build_sum), k=build_num))
    # df = pd.DataFrame(random_candidate_loc_id).T
    # output_name = 'build_num_choose_' + str(build_num) + '.csv'
    # df.to_csv(output_name, index=False)    
    
    data = Data.Data()
    # data.read_data(file_name,file_name_ohca,loc_num=loc_num,dist_limit=dist_limit,build_num=build_num)   
    data.read_npy(file_name,file_name_ohca,dist_limit=dist_limit,build_num=build_num)   
    print('read finishing !')
    # data = np.load('indicator_i_j.npy')
       
    for loc_num in loc_num_list: 
        output_name = 'build_num_choose_' + str(loc_num)+ '_set_' + str(10) + '.npy'
        random_candidate_loc_id = np.load(output_name).astype(np.int64)
        deploy_decision_coverage = np.zeros(build_num_choose_cnt)
        deploy_decision = np.zeros((build_num_choose_cnt, loc_num))
        deploy_decision_survivalrate = np.zeros((build_num_choose_cnt,len(data.ohca_lat)))
        deploy_decision_survivalrate_average = np.zeros(build_num_choose_cnt)
        for cnt in range(build_num_choose_cnt):
            model_handler = ModelBuilder.ModelBuilder()
            candidate_loc_id = random_candidate_loc_id[cnt]
            model_handler.build_IP(data,candidate_loc_id,loc_num)
            print('{} = {}'.format('obj_val', model_handler.obj_val), end='')
            print()
            print('{} = {}'.format('run_time', model_handler.run_time), end='')
            print()
            print('{} = {}'.format('deployment_decision', model_handler.deploy_decision), end='')
            print()
            deploy_decision[cnt] = np.array(model_handler.deploy_decision)   
            ohca_cover_cnt_predict = 0
            for ohca in range(len(data.ohca_lat)):
                iscover = 0
                min_dist = np.inf
                for i in range(len(model_handler.deploy_decision)):
                    loc = model_handler.deploy_decision[i]
                    dist_loc_ohca = data.haversine(data.loc_lat[loc],data.loc_lon[loc],data.ohca_lat[ohca],data.ohca_lon[ohca])
                    if dist_loc_ohca <= min_dist:
                        min_dist = dist_loc_ohca
                    if dist_loc_ohca <= dist_limit:
                        iscover = 1
                t_loc_ohca = min_dist / 300 * 1000
                if t_loc_ohca <= 4:
                    s_loc_ohca = (1 + np.exp(-0.26 + 0.106 * t_loc_ohca + 0.139 * 10.5))**(-1)
                else:
                    s_loc_ohca = 0  
                deploy_decision_survivalrate[cnt][ohca] = s_loc_ohca   
                if iscover == 1:
                    ohca_cover_cnt_predict += 1   
            deploy_decision_coverage[cnt] = ohca_cover_cnt_predict
            print(deploy_decision_survivalrate[cnt])
            deploy_decision_survivalrate_average[cnt] = np.average(deploy_decision_survivalrate[cnt])
        
        output_name = 'results/deployment_decision_' + str(loc_num)+ '_set_' + str(build_num_choose_cnt)
        np.save(output_name,deploy_decision)   
        output_name = 'results/deployment_decision_coverage_' + str(loc_num)+ '_set_' + str(build_num_choose_cnt)
        np.save(output_name,deploy_decision_coverage) 
        output_name = 'results/deploy_decision_survivalrate_' + str(loc_num)+ '_set_' + str(build_num_choose_cnt)
        np.save(output_name,deploy_decision_survivalrate)
        output_name = 'results/deploy_decision_survivalrate_average_' + str(loc_num)+ '_set_' + str(build_num_choose_cnt)
        np.save(output_name,deploy_decision_survivalrate_average)
                            
        # df = pd.DataFrame(deploy_decision).T
        # output_name = 'deploy_decision_' + str(build_num) + '.csv'
        # df.to_csv(output_name, index=False) 
        print('model finishing _ ',loc_num) 
        
        # ohca_cover_cnt_predict = 0
        # # ohca_cover_cnt_random = 0
        # random_numbers = {}
        # for i in range(100):
        #     random_numbers[i] = random.choices(range(build_num), k=loc_num)
        # ohca_cover_cnt_random = {}
'''
  (1 + e^{-0.26 + 0.106 \cdot t_{\text{aed}} + 0.139 \cdot t_{\text{cpr}}})^{-1}, & t_{\min} < 4, \\
    0, & t_{\min} \geq 4.
'''        

    # for ohca in range(len(data.ohca_lat)):
    #     iscover = 0
    #     for i in range(len(model_handler.deploy_decision)):
    #         loc = model_handler.deploy_decision[i]
    #         dist_loc_ohca = data.haversine(data.loc_lat[loc],data.loc_lon[loc],data.ohca_lat[ohca],data.ohca_lon[ohca])
    #         if dist_loc_ohca <= dist_limit:
    #             iscover = 1
    #     if iscover == 1:
    #         ohca_cover_cnt_predict += 1 
            
            
    # for j in range(100):
    #     ohca_cover_cnt_random[j] = 0
    #     for ohca in range(len(data.ohca_lat)):
    #         iscover = 0
    #         for i in range(len(random_numbers[j])):
    #             loc = random_numbers[j][i]
    #             dist_loc_ohca = data.haversine(data.loc_lat[loc],data.loc_lon[loc],data.ohca_lat[ohca],data.ohca_lon[ohca])
    #             if dist_loc_ohca <= dist_limit:
    #                 iscover = 1
    #         if iscover == 1:
    #             ohca_cover_cnt_random[j] += 1
    # print('{} : {}'.format('ohca_cover_cnt_predict', ohca_cover_cnt_predict), end='')
    # print()
    # print('{} : {}'.format('ohca_cover_cnt_random', ohca_cover_cnt_random), end='')
    # print()
        
    

