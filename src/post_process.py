#!/usr/bin/env python
# coding=utf-8
import time

class post_proc(object):
    def __init__(self,filename):
        self.filename = filename
    
    def time_post_process(self,res):
        f = open(self.filename,'a')
        f.write(res+"\n")
        f.close()
        time.sleep(10)
