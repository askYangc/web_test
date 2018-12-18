# -*- coding: utf-8 -*-


class QueryIndexType:
    QueryIndexHomeId = 1
    QueryIndexUserId = 2
    QueryIndexSn = 3

class FlowQueryMsgStr:
    LOG_NONE = 0
    LOG_USER_MODIFY = 1
    LOG_USER_ROLE_MODIFY = 2
    LOG_USER_PHONEINFO_MODIFY = 3
    LOG_USER_WIDGETKEY_MODIFY = 4
    LOG_USER_MAIL_BIND = 5
    LOG_USER_MAIL_UNBIND = 6
    LOG_USER_REPLACE = 7

    LOG_HOME_CREATE =  8
    LOG_HOME_DELETE = 9
    LOG_HOME_SN_JOIN = 10
    LOG_HOME_SN_LEAVE = 11
    LOG_HOME_SN_RESETCT_UPDATE = 12
    LOG_HOME_SN_MODITYPASSWD =13
    LOG_HOME_NAME_MODITY = 14
    LOG_HOME_OWNER_MODITY = 15
    LOG_HOME_MASTER_MODITY = 16
    LOG_HOME_APPROVAL_MODITY = 17
    LOG_HOME_USER_LEAVE = 18
    LOG_HOME_USER_JOIN = 19
    LOG_HOME_USER_EDIT = 20
    LOG_HOME_USER_LEVEL_EDIT = 21
    LOG_HOME_LINKAGE_ADD = 22
    LOG_HOME_LINKAGE_EDIT = 23
    LOG_HOME_LINKAGE_DEL = 24
    LOG_HOME_LINKAGE_EXEC = 25
    LOG_HOME_LABELADD = 26
    LOG_HOME_LABELDEL = 27
    LOG_HOME_LABEL_SNADD = 28
    LOG_HOME_LABEL_SNDEL = 29
    LOG_HOME_DICTADD = 30
    LOG_HOME_DICTDEL = 31

    LOG_MAX = 32