#-*-coding:utf-8-*-
from .sigleton import singleton
import time

@singleton
class WikiManager(object):
    def __init__(self):
        self._wiki_dict = {}
        self._has_changed = True

    def set_changed(self, has_changed):
        self._has_changed = has_changed

    def get_wiki_content(self, node_name):
        if self._has_changed:
            self._wiki_dict.clear()
            self._has_changed = False
        if node_name not in self._wiki_dict:
            self._wiki_dict[node_name] = WikiContent(node_name)
        return self._wiki_dict[node_name]

    def remove_wiki_content(self, node_name):
        if node_name in self._wiki_dict:
            del self._wiki_dict[node_name]

class WikiContent(object):
    def __init__(self, node_name):
        self._node_name = node_name
        self._content_list = []
        self.update_content_list()

    def get_content_list(self):
        return self._content_list

    def update_content_list(self):
        from .views import get_content, get_overview_info
        from .models import *
        self._content_list = []
        table_content0, macth_val_list1 = get_content(CM_Application, "ChineseName", [self._node_name])
        table_content1, macth_val_list2 = get_content(CM_Application_Maintainer, "AppID", macth_val_list1)
        table_content2, match_val_list3 = get_content(Appserver, "AppID", macth_val_list1)
        table_content3, match_val_list4 = get_content(CM_Users, "AppServerID", match_val_list3)
        table_content4, match_val_list5 = get_content(Config_File, "AppServerID", match_val_list3)
        table_content5, match_val_list6 = get_content(Log_File, "AppServerID", match_val_list3)
        table_content6, match_val_list7 = get_content(Server_Process_Pool, "AppServerID", match_val_list3)
        table_content7, match_val_list8 = get_content(Software, "AppServerID", match_val_list3)
        table_content8, match_val_list9 = get_content(Weblogic, "SoftwareID", match_val_list8)
        table_content9, match_val_list10 = get_content(Weblogic_Jdbc, "WeblogicID", match_val_list9)
        table_content10, match_val_list11 = get_content(Weblogic_Server, "WeblogicID", match_val_list9)
        table_content11, match_val_list12 = get_content(Weblogic_Jdbc_Map, "ServerID", match_val_list11)
        table_content12, match_val_list13 = get_content(Weblogic_App, "ServerID", match_val_list11)
        table_content13, match_val_list14 = get_content(DB, "SoftwareID", match_val_list8)
        table_content14, match_val_list15 = get_content(MQ, "SoftwareID", match_val_list8)
        table_content15, match_val_list16 = get_content(Tomcat, "SoftwareID", match_val_list8)
        table_content16, match_val_list17 = get_content(Apache, "SoftwareID", match_val_list8)
        table_content17, match_val_list18 = get_content(Other, "SoftwareID", match_val_list8)
        device_id_list = set()
        for app_server in match_val_list3:
            try:
                device_id_list.add(app_server.DeviceID.DeviceID)
            except:
                pass
        device_id_list = list(device_id_list)

        cluser_id_list = set()
        for app_server in match_val_list3:
            try:
                cluser_id_list.add(app_server.CluserID.CluserID)
            except:
                pass
        cluser_id_list = list(cluser_id_list)

        table_content18, match_val_list19 = get_content(Device, "DeviceID", device_id_list)
        table_content19, match_val_list20 = get_content(server_detail, "DeviceID", match_val_list19)
        table_content20, match_val_list21 = get_content(storage_detail, "DeviceID", match_val_list19)
        table_content21, match_val_list22 = get_content(NetDevice_detail, "DeviceID", match_val_list19)
        table_content22, match_val_list23 = get_content(Equipment_detail, "DeviceID", match_val_list19)

        table_content23, match_val_list_cluser = get_content(Cluser, "CluserID", cluser_id_list)  # table_content_cluser
        table_content24, match_val_list_img = get_content(ImageStore, "AppID", macth_val_list1)  # table_content_img
        table_content25, match_val_list_mount = get_content(Mount, "AppServerID", match_val_list3)  # table_content_mount
        table_content26, match_val_list__conf_item = get_content(Config_Item, "ConfigName", match_val_list5)  # table_content_conf_item
        table_content27, match_val_License = get_content(License, "AppID", macth_val_list1)  # table_content_License
        table_content28, match_val_list_LB = get_content(LB, "AppID", macth_val_list1)  # table_content_LB
        table_content29, match_val_list_LB_Member = get_content(LB_Member, "AppServerID", match_val_list3)  # table_content_LB_member
        table_content30 = get_overview_info(self._node_name)  # table_overview

        for i in range(31):
            varStr = '=table_content' + str(i)
            exec ('var' + varStr)
            self._content_list.append(var)

