#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gitlab,configparser,urllib2,urllib

"""
将本地运行的publickey上传到gitlab

"""


class uploadkey:

    #获取服务器配置信息
    def getServerConfig(self):
        serverConfig = configparser.ConfigParser()
        serverConfig.read('config/server.ini')
        host = serverConfig.get('gitlab_info','host')
        login = serverConfig.get('gitlab_info','username')
        pwd = serverConfig.get('gitlab_info','password')

    #封装gitlab get请求
    def gitPost(self,host,params):
        pass
