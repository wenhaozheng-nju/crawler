#!/usr/bin/env python
# coding=utf-8

from trigger import trigger
from process_website import website
from post_process import post_proc
from urls import url_manage
import time

slot = 10

def process(start_url):
    w = website()
    u = url_manage(start_url)
    process_func = w.qq_news_process
    t = trigger(slot)
    trigger_func = t.url_trigger
    p = post_proc("../data/result.csv")
    post_proc_func = p.save_result_process
    while 1:
        if trigger_func(u):
            url = u.get_url()
            res = process_func(url)
            post_proc_func(res,url,u)
        time.sleep(10)

if __name__ == "__main__":
    process("http://news.qq.com/")


