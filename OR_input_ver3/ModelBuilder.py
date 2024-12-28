"""
AED_deployment_model
Author: Kexin Cao
Institute: Tsinghua University
Date: 20241220 
"""


from gurobipy import *
import time

class ModelBuilder(object):
    
    def __init__(self):
        self.data = None
        
        self.x_i = {}
        self.cons_dist = {}

        self.deploy_decision = []
        
        self.obj_val = 0
        self.run_time = 0
                
    def build_IP(self, data, candidate_loc_id, loc_num):
        start_time = time.time()
        self.data = data
        self.IP_model = Model('IP_model')
        obj = LinExpr()
        lhs = LinExpr()
        for loc_id in candidate_loc_id:
            i = loc_id
            self.x_i[i] = self.IP_model.addVar(lb = 0, ub = 1, vtype = GRB.BINARY, name = 'x_' + str(i))
            obj.addTerms(data.loc_score[i], self.x_i[i])
            lhs.addTerms(1, self.x_i[i])
            # if i % 200 == 0:
            #     print(i) 
        self.IP_model.setObjective(obj, GRB.MAXIMIZE)    
        for loc_id in candidate_loc_id:
            for loc_id_j in candidate_loc_id:
                i = loc_id
                j = loc_id_j
                if j != i and data.indicator_i_j[i,j] == 1:
                    self.cons_dist[i,j] = self.IP_model.addConstr(self.x_i[i] + self.x_i[j] <= 1, name = 'cons_dist' + '_' + str(i) + '_' + str(j))
            # if i % 200 == 0:
            #     print(i) 
        
        self.cons_sum = self.IP_model.addConstr(lhs <= loc_num, name = 'cons_sum')
        self.IP_model.setParam('OutputFlag', 1) 
        self.IP_model.setParam('Presolve', 1)   
        # self.IP_model.setParam('Threads', 16)       # 设置使用16个线程
        # self.IP_model.setParam('MIPFocus', 2)       # 关注求解器的节省时间性能
        # self.IP_model.setParam('Presolve', 2)       # 开启预求解
        # self.IP_model.setParam('Cuts', 2)           # 强化切割平面
        # self.IP_model.setParam('Heuristics', 0.5)   # 调高启发式的方法比例
        # self.IP_model.setParam('ImproveStartTime', 1200) # 设置改善开始时间
        finish_time = time.time() - start_time 
        print('model construction time:',finish_time)  
        self.IP_model.optimize()  
        # self.IP_model.write('IP_model.lp')
        self.obj_val = self.IP_model.ObjVal
        self.run_time = self.IP_model.run_time
        for loc_id in candidate_loc_id:
            if self.x_i[loc_id].x >= 0.5:
                self.deploy_decision.append(loc_id) 
        
                   
                    
                    
                    
                    
                    
                    
                    