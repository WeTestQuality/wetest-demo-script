# -*- coding: utf-8 -*-
#
# Copyright 2022 WeTest. All rights reserved.

def get_i18n_string(locale, s):
    cn_strings = {'GENERAL': '通用',
                  "VPN": "VPN",
                  "VPN_AND_DEVICE_MANAGEMENT": "VPN与设备管理",
                  "ADD_VPN_CONFIGURATION": "添加 VPN 配置…",
                  "ADD_VPN_CONFIGURATION_IOS13": "添加VPN配置…",
                  "TYPE": "类型",
                  "ADD_CONFIGURATION": "添加配置",
                  "DESCRIPTION": "描述",
                  "SERVER": "服务器",
                  "ACCOUNT": "帐户",
                  "PASSWORD": "密码",
                  "SECRET": "密钥",
                  "DONE": "完成",
                  "STATUS": "状态",
                  "NOT_CONNECTED": "未连接",
                  "STATUS_CONNECTED": "状态, 已连接",
                  "STATUS_NOT_CONNECTED": "状态, 未连接",
                  "VPN_CONNECTION": "VPN连接",
                  "L2TP_VPN_SERVER_DID_NOT_RESPOND": "L2TP-VPN服务器未响应。",
                  "MORE_INFORMATION": "更多信息",
                  "DELETE_VPN": "删除 VPN",
                  "DELETE_VPN_IOS13": "删除VPN",
                  "DELETE_VPN_QUESTION_MARK": "要删除 VPN 吗？",
                  "DELETE_VPN_QUESTION_MARK_IOS13": "要删除VPN吗？",
                  "DELETE": "删除"}

    en_strings = {'GENERAL': 'General',
                  "VPN": "VPN",
                  "VPN_AND_DEVICE_MANAGEMENT": "VPN & Device Management",
                  "ADD_VPN_CONFIGURATION": "Add VPN Configuration…",
                  "ADD_VPN_CONFIGURATION_IOS13": "Add VPN Configuration…",
                  "TYPE": "Type",
                  "ADD_CONFIGURATION": "Add Configuration",
                  "DESCRIPTION": "Description",
                  "SERVER": "Server",
                  "ACCOUNT": "Account",
                  "PASSWORD": "Password",
                  "SECRET": "Secret",
                  "DONE": "Done",
                  "STATUS": "Status",
                  "NOT_CONNECTED": "Not Connected",
                  "STATUS_CONNECTED": "Status, Connected",
                  "STATUS_NOT_CONNECTED": "Status, Not Connected",
                  "VPN_CONNECTION": "VPN Connection",
                  "L2TP_VPN_SERVER_DID_NOT_RESPOND": "The L2TP-VPN server did not respond.",
                  "MORE_INFORMATION": "More Information",
                  "DELETE_VPN": "Delete VPN",
                  "DELETE_VPN_QUESTION_MARK": "Delete VPN?",
                  "DELETE_VPN_QUESTION_MARK_IOS13": "Delete VPN?",
                  "DELETE": "Delete"}

    if locale == 'cn':
        return cn_strings[s]
    if locale == 'en':
        return en_strings[s]
