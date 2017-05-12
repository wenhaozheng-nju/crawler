#!/usr/bin/env python
# coding=utf-8
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

USER_AGENTS = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A']

phantomjs_path = '/Users/zhouyh/phantomjs-2.1.1-macosx/bin/phantomjs'


class Website(object):

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.loadImages"] = False
    dcap["phantomjs.page.settings.userAgent"] = (random.choice(USER_AGENTS))
    driver = webdriver.PhantomJS(phantomjs_path, desired_capabilities=dcap)

    def __init__(self):

        pass
        # self.fetcher = Fetcher(
        #             user_agent='phantomjs', # user agent
        #             phantomjs_proxy='http://localhost:12306', # phantomjs url
        #             pool_size=10, # max httpclient num
        #             async=False
        #     )

    def weibo_hot_process(self,url):
        soup = self.visit_url(url)
        content = soup.find(name='div',attrs={'class','WB_innerwrap'})
        texts = []
        for div in content.findAll(name='div',attrs={'class','info_box'}):
            text = div.get_text()
            text = text.replace("\n","\t")
            texts.append(text)
        return texts

    @staticmethod
    def qq_news_process(url):
        soup = Website.visit_url(url)
        url_ele = url.split("/")
        domain_name = url_ele[2]
        #print("domin_name is:",domain_name) #test
        if len(url_ele) >= 3 and url_ele[-2].isdigit() and url_ele[-3] == "a":
            print ("it is content page!")
            content = Website.handle_content_page(soup)
            content['time'] = url_ele[-2]
            return content
        else:
            hrefs = []
            for a in soup.findAll(name='a'):
                try:
                    href = a['href']
                    if href.find(domain_name) >=0:
                        hrefs.append(href)
                except:
                    pass
            #print(hrefs) #test
            return hrefs
        # return url

    @staticmethod
    def visit_url(url,comment_flag=False):
        # content_dict = self.fetcher.phantomjs_fetch(url)
        # print content_dict
        Website.driver.get(url)
        if comment_flag:
            Website.driver.switch_to.frame('commentIframe')   ##orz
        soup = BeautifulSoup(Website.driver.page_source,'html.parser')
        print(url,"is visited done!")
        return soup

    @staticmethod
    def handle_content_page(page):
        content = {}
        content['title'] = page.find('title').get_text()
        content['body'] = ""
        for p in page.findAll(name='p'):
            p_attrs = dict(p.attrs)
            for key in p_attrs:
                val = p_attrs[key]
                if isinstance(val,list):
                    val = val[0]
                if val.lower().startswith('text') and p.script is None: # p maybe contain video
                    #print val
                    content['body'] += p.get_text().strip()+"\t"

        # print content['body']

        content['body'] = content['body'].replace("\n","\t")
        comment_url = ""
        for a in page.findAll(name='a'):
            try:
                if a['id'].find('cmt') >= 0: # id could be cmtLink or cmtNum
                    comment_url = a['href']
            except:
                pass
        if len(comment_url) == 0:
            content['comment'] = []
        else:
            # comment_url = comment_url['href']
            comment_soup = Website.visit_url(comment_url,True)
            content['comment'] = []
            for p in comment_soup.findAll(name='p'):
                content['comment'].append(p.get_text().strip())
        content['comment'] = "\t".join(content['comment'])
        return content
    

if __name__ == '__main__':
    w = Website()
    soup = w.visit_url("http://news.qq.com/a/20160418/023091.htm")
    w.handle_content_page(soup)
    # w.visit_url("http://coral.qq.com/1909556775",True)