#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gitcommand import setupkey

"""

执行获取工程并clone代码

"""

if __name__ == '__main__':

    test = setupkey.sshkey()
    test.addkey()
    test.getPublicString()
    test.uploadkey()



