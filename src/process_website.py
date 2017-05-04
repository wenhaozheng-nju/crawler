#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup


class website(object):
    
    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def weibo_hot_process(self,url):
        self.driver.get(url)
        html_content = self.driver.page_source
        print ("content is:",html_content)
        soup = BeautifulSoup(html_content)
        content = soup.find(name='div',attrs={'class','WB_innerwrap'})
        texts = []
        for div in content.findAll(name='div',attrs={'class','info_box'}):
            text = div.get_text()
            text = text.replace("\n","\t")
            texts.append(text)
        return texts


    
