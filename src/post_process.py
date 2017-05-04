#!/usr/bin/env python
# coding=utf-8
import time
import pandas as pd
import os

class post_proc(object):
    def __init__(self,filename):
        self.filename = filename
        if os.path.exists(self.filename):
            os.remove(self.filename)

    
    def time_post_process(self,res):
        f = open(self.filename,'a')
        f.write(res+"\n")
        f.close()
        time.sleep(10)

    def save_result_process(self,res,read_url,url_pool):
        url_pool.url_done(read_url)
        if isinstance(res,dict):
            if os.path.exists(self.filename):
                d = pd.read_csv(self.filename,encoding='utf-8')
            else:
                d = pd.DataFrame(columns=list(res.keys()))
            d = d.append(pd.Series(res),ignore_index=True)
            d.to_csv(self.filename,index=False,encoding='utf-8')

        elif isinstance(res,list):
            url_pool.add_url(res)

