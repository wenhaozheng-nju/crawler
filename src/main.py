#!/usr/bin/env python
# coding=utf-8

from trigger import Trigger
from process_website import Website
from post_process import post_proc
from urls import url_manage
import time
from pyspark import SparkConf, SparkContext

slot = 10


def process(start_url):

    u = url_manage(start_url)

    w = Website()
    process_func = w.qq_news_process

    t = Trigger(slot)
    trigger_func = t.url_trigger

    p = post_proc("../data/result.csv")
    post_proc_func = p.save_result_process

    conf = SparkConf().setMaster("local[8]").setAppName("Crawler")
    sc = SparkContext(conf=conf)

    while 1:
        if trigger_func(u):
            urls = sc.parallelize(u.get_url_queue())
            results = urls.map(process_func)
            print results.collect()
            for res, url in zip(results.collect(), urls.collect()):
                print res, url
                post_proc_func(res, url, u)
        time.sleep(1)

    sc.stop()


if __name__ == "__main__":
    process("http://news.qq.com/")


