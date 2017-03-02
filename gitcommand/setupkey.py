#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,configparser
reload(sys)


"""
目的是生成1个private key和1个public key在本地,配置sshKey环境

"""


class sshkey():

        def __init__(self):
            self.sshkey = ''

        #获取config.ini中的配置
        def getPath(self):
            config = configparser.ConfigParser()
            config.read('config/config.ini')
            path = config.get('save_path','path')
            readPath = config.get('save_path','path2')
            return path , readPath

        #执行cmd命令生成public_key和private_key
        def addkey(self):
            sys.setdefaultencoding('utf-8')
            addkey = 'ssh-keygen –t rsa'+ '- f'+self.getPath()[1]+'/keyPath'
            os.popen(addkey)

        #获取.pub文件中的字符串
        def getPublicString(self):
            loadPath = self.getPath()[1]
            file = open(loadPath,'r+')
            keyString = file.read()
            return keyString

        #将keystring上传到gitlab
        def uploadString(self):
            serverConfig = configparser.ConfigParser()
            serverConfig.read('config/server.ini')
            host = serverConfig.get('gitlab_info', 'host')
            cmd = 'ssh-copy -id '+' -i liqi@danlu.com@'+ host
