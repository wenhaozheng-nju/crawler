#!/usr/bin/env python
# coding=utf-8

from trigger import trigger
from process_website import website
from post_process import post_proc 
import time

slot = 10

def process(url):
    w = website()
    process_func = w.weibo_hot_process
    t = trigger(slot)
    trigger_func = t.time_trigger
    p = post_proc("../data/result.txt")
    post_proc_func = p.time_post_process
    while 1:
        if trigger_func():
            res = process_func(url)
            post_proc_func(res)
        else:
            time.sleep(10)

if __name__ == "__main__":
    process("http://weibo.com/?category=1760")


