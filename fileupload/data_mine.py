# encoding: utf-8#
from fileupload.models import SysConfInfo,VerConfInfo,SysDataMineInfo
UN_NEED_SYCN = ["ETL","IMIX中间件","IMIX","IMIX协议"]#无需同步的系统列表
DATA_TYPE = {"成交":"交易数据","行情":"交易数据","报价":"交易数据","交易明细":"交易数据","回购":"交易数据",
              "会员信息":"基础数据","机构信息":"基础数据","机构权限":"基础数据","节假日":"基础数据","债券":"基础数据","标志位":"基础数据","账户信息":"基础数据",
              "日报":"统计数据","月报":"统计数据","统计":"统计数据","历史":"统计数据","结算":"统计数据",
              "确认":"交易后数据","清算":"交易后数据","账务":"交易后数据",
              }
INTERACTION_METHOD = {"ETL":"ETL",
                      "IMIX":"IMIX"
                      }
TYPE = {"ETL":"定时",
        "IMIX":"实时",
        }

def get_mine_data_type_value(mine_str,mine_dict):
    '''监测所有的字符串里面,是否包含某几个key,若包含则返回相应的值,专门返回交易数据类型与接口（数据交互依赖）'''
    return_val_set = set() 
    for word in mine_dict.keys():
        if word in mine_str:
            return_val_set.add(mine_dict[word])
    return list(return_val_set)
def get_conn_method(mine_str):
    '''挖掘链接方法和type'''
    for word in INTERACTION_METHOD.keys():
        if word in mine_str:
            return word,TYPE[word]
    return "",""
def update_data_without_db(system_info):
    '''检测所得系统信息中,有无可以更新的地方'''
    sys_info_dict = {}
    for source_system in system_info:
        for target_system in system_info[source_system]:
            node_info_list = system_info[source_system][target_system]
            for node_info in node_info_list:
                sys_info_dict.setdefault(source_system+"\t"+target_system,set()).add(node_info)
                sys_info_dict.setdefault(target_system+"\t"+source_system,set()).add(node_info)
    for source_target in sys_info_dict:
        source,target = source_target.split("\t")
        if source not in system_info:
            system_info[source] = {}
        system_info[source][target] = list(sys_info_dict[source_target])
def save_mine_into_db(source_name,target_name,data_info_list):
    
    '''将挖掘出来的数据存放到db里面'''
    for data_info in data_info_list:
        tmp_data_type,data_interaction_detail,conn,conn_method,tmp_from_info = data_info.split("\t")
        new_data = SysDataMineInfo(node_source=source_name,
                                   node_target=target_name,
                                   data_type=tmp_data_type,
                                   conn=data_interaction_detail,
                                   conn_method=conn,
                                   type=conn_method,
                                   from_info = tmp_from_info
                                   )
        new_data.save()
        
        
      
def sycn_sys_ver_info(system_info,ver_info):
    SysDataMineInfo.objects.all().delete()#删除存储挖掘信息的数据
    update_data_without_db(system_info.sys_info)#完成闭包
    '''同步版本和系统之间的协同性,以版本更新系统'''
    pair_dict = {}
    data_info_from_version_info = {}
    for source_name in ver_info:
        if source_name not in UN_NEED_SYCN:#仅有不在禁止列表中的源系统才会被考虑
            for s_v in ver_info[source_name]:#版本源
                for target_name in ver_info[source_name][s_v]:#版本目标
                    if target_name not in UN_NEED_SYCN:#仅有不在禁止列表中的目标系统才会被考虑
                        data_info_list = []
                        data_info_from_version_info_list = []#仅在data类型为0时使用
                        
                        for t_v in ver_info[source_name][s_v][target_name]:
                            #t_v = t_v if t_v != "" else "最新版本"
                            if_test,if_sync = ver_info[source_name][s_v][target_name][t_v].split("\t")[1:3]
                            if if_sync == 'Y' or if_sync == 'y':
                                depend_detail,data_interaction_detail = ver_info[source_name][s_v][target_name][t_v].split("\t")[-2:]
                                from_info = "#{}{}与{}{}的版本文件.   数据交互备注:{};   数据依赖备注:{}".format(target_name,t_v,source_name,s_v,data_interaction_detail,depend_detail)
                                data_type_list = get_mine_data_type_value(data_interaction_detail,DATA_TYPE)
                                conn,conn_method = get_conn_method(depend_detail)
                                for data_type in data_type_list:
                                    data_info_list.append("\t".join([data_type,data_interaction_detail,conn,conn_method,from_info]))
                                data_info_from_version_info_list.append(from_info)
                        '''数据信息'''
                        if len(data_info_from_version_info_list) != 0:
                            if source_name+"\t"+target_name not in pair_dict:
                                pair_dict[source_name+"\t"+target_name] = []
                            pair_dict[source_name+"\t"+target_name].extend(data_info_list)#对各个目标版本提出统一一份
                            '''备注信息'''
                            if source_name+"\t"+target_name not in data_info_from_version_info:
                                data_info_from_version_info[source_name+"\t"+target_name] = []
                            data_info_from_version_info[source_name+"\t"+target_name].extend(data_info_from_version_info_list)#对各个目标版本提出统一一份
                        
    for pair_node in pair_dict:
        source_name,target_name = pair_node.split("\t")
        data_info_list = pair_dict[pair_node]
        if source_name not in system_info.sys_info:
            system_info.sys_info[source_name] = {}
        if target_name not in system_info.sys_info[source_name]:
            if len(data_info_list) == 0:
                data_info_list = []
                for from_info in data_info_from_version_info[pair_node]:
                    data_info_list.append("{0}\t{1}\t{2}\t{3}\t{4}".format("","","","",from_info))
            system_info.sys_info[source_name][target_name] = data_info_list
            save_mine_into_db(source_name,target_name,data_info_list)#将挖掘出来的数据保存到数据库中
    update_data_without_db(system_info.sys_info)#完成闭包
            
