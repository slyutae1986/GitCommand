#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,configparser
reload(sys)

"""
目的是执行文件操作

"""


class gitclone:

    def  login(self,username,password):
        gitconfig = configparser.ConfigParser
        gitconfig.read('config/server.ini')


