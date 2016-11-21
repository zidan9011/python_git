# encoding: utf-8#
'''
Created on 2015年5月18日

@author: yzd
'''
data_type_list = ["交易后数据","交易数据","基础数据","曲线数据","行情数据","统计数据","其他数据类型"]
data_method_list = ["ETL","IMIX","MQ","FTP(SFTP)","DBLink","其他接口方式"]#注FTP(SFTP)可能在数据中是分开的,需要将这两个合并

dataex_type_list = ["核心交易体系","公共服务体系","交易后服务体系","信息服务体系","各体系共通"]
dataex_method_list = ["ETL","IMIX","FTS"]

DATAEX_METHOD_LEGEND_MAP = {"ETL":"ETL",
                          "IMIX":"IMIX",
                          "FTS":"FTS"
                          }

DATAEX_DATA_LEGEND_MAP = {"各体系共通":"各体系共通",
                          "公共服务体系":"公共服务体系",
                          "核心交易体系":"核心交易体系",
                          "交易后服务体系":"交易后服务体系",
                          "信息服务体系":"信息服务体系",
                          }
SYSTEM_DATA_LEGEND_MAP = {"交易数据":"交易数据",
                          "基础数据":"基础数据",
                          "交易后数据":"交易后数据",
                          "曲线数据":"曲线数据",
                          "行情数据":"行情数据",
                          "统计数据":"统计数据"
                          }
SYSTEM_METHOD_LEGEND_MAP = {"ETL":"ETL",
                          "IMIX":"IMIX",
                          "MQ":"MQ",
                          "FTP":"FTP(SFTP)",
                          "SFTP":"FTP(SFTP)",
                          "DBLink":"DBLink"
                          }
class Legend_Info_System():
    def __init__(self,s_info_request_name):
        self.s_info_target = s_info_request_name
        self.node_data_type_info = {}#存放 类型-节点 信息
        self.node_conn_method_info = {}
        self.get_type_dict()
    def get_type_dict(self):
        '''将输入的target数据,加载到legend信息中'''
        for target in self.s_info_target:
            #self.s_info_target[target] = self.s_info_target[target]
            '''补充数据细节到另外四个数据存储器中'''
            for link_info in self.s_info_target[target]:#对于两节点的交互信息
                tmp_info = link_info.split("\t")
                if tmp_info[0] in SYSTEM_DATA_LEGEND_MAP:
                    self.node_data_type_info.setdefault(SYSTEM_DATA_LEGEND_MAP[tmp_info[0]],set()).add(target)
                else:
                    self.node_data_type_info.setdefault("其他数据类型",set()).add(target)
                if tmp_info[2] in SYSTEM_METHOD_LEGEND_MAP:
                    self.node_conn_method_info.setdefault(SYSTEM_METHOD_LEGEND_MAP[tmp_info[2]],set()).add(target)
                else:
                    self.node_conn_method_info.setdefault("其他接口方式",set()).add(target)
    def get_legend_list(self):
        #给legend,category,node_info使用的      
        data_legend = [val for val in data_type_list if val in self.node_data_type_info.keys()]
        method_legend = [val for val in data_method_list if val in self.node_conn_method_info.keys()]
        full_category = data_legend+method_legend#展示在category上
        full_legend = data_legend+[""]+method_legend#展示在legend上
        legend_node_info = []
        category_index = 2
        for type in data_legend:
            for node_name in self.node_data_type_info[type]:
                legend_node_info.append("{category:"+str(category_index)+",name:'"+node_name+"', value : 13},")
            category_index += 1
        for type in method_legend:
            for node_name in self.node_conn_method_info[type]:
                legend_node_info.append("{category:"+str(category_index)+",name:'"+node_name+"', value : 13},")
            category_index += 1       
        return full_legend,full_category,legend_node_info

class DataEX_Legend_Info_System_old():
    def __init__(self,s_info_request_name):
        self.s_info_target = s_info_request_name
        self.node_data_type_info = {}#存放 类型-节点 信息
        self.node_conn_method_info = {}
        self.get_type_dict()
    def get_type_dict(self):
        '''将输入的target数据,加载到legend信息中'''
        for target in self.s_info_target:
            #self.s_info_target[target] = self.s_info_target[target]
            '''补充数据细节到另外四个数据存储器中'''
            for link_info in self.s_info_target[target]:#对于两节点的交互信息
                tmp_info = link_info.split("\t")
                if tmp_info[-1] in DATAEX_DATA_LEGEND_MAP:
                    self.node_data_type_info.setdefault(DATAEX_DATA_LEGEND_MAP[tmp_info[-1]],set()).add(target)
                else:
                    self.node_data_type_info.setdefault("其他服务体系",set()).add(target)
    def get_legend_list(self):
        #给legend,category,node_info使用的      
        data_legend = [val for val in dataex_type_list if val in self.node_data_type_info.keys()]
        full_category = data_legend#展示在category上
        full_legend = data_legend#展示在legend上
        legend_node_info = []
        category_index = 2
        for type in data_legend:
            for node_name in self.node_data_type_info[type]:
                legend_node_info.append("{category:"+str(category_index)+",name:'"+node_name+"', value : 13},")
            category_index += 1   
        return full_legend,full_category,legend_node_info    
    
    
    
    
class DataEX_Legend_Info_System():
    def __init__(self,s_info_request_name):
        self.s_info_target = s_info_request_name
        self.node_data_type_info = {}#存放 类型-节点 信息
        self.node_conn_method_info = {}
        self.get_type_dict()
    def get_type_dict(self):
        '''将输入的target数据,加载到legend信息中'''
        for target in self.s_info_target:
            #self.s_info_target[target] = self.s_info_target[target]
            '''补充数据细节到另外四个数据存储器中'''
            for link_info in self.s_info_target[target]:#对于两节点的交互信息
                tmp_info = link_info.split("\t")
                if tmp_info[-1] in DATAEX_METHOD_LEGEND_MAP:
                    self.node_data_type_info.setdefault(DATAEX_METHOD_LEGEND_MAP[tmp_info[-1]],set()).add(target)
                else:
                    self.node_data_type_info.setdefault("其他",set()).add(target)
    def get_legend_list(self):
        #给legend,category,node_info使用的      
        data_legend = [val for val in dataex_method_list if val in self.node_data_type_info.keys()]
        full_category = data_legend#展示在category上
        full_legend = data_legend#展示在legend上
        legend_node_info = []
        category_index = 2
        for type in data_legend:
            for node_name in self.node_data_type_info[type]:
                legend_node_info.append("{category:"+str(category_index)+",name:'"+node_name+"', value : 13},")
            category_index += 1   
        return full_legend,full_category,legend_node_info    