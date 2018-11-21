#!/usr/bin/env/ python 
# -*- coding:utf-8 -*-
# Author:Mr.Xu

import asyncio
import requests
import time
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from multiprocessing import Process
from selenium import webdriver
from Csdn_spider.config import *

class MyCsdn():
    def __init__(self):
        self.url = "https://blog.csdn.net/m0_37903789"
        self.wait_time = 0
        self.task_num = 0
        self.proxy = self.get_proxy()
        self.ua = UserAgent()
        self.headers = {
            "User-Agent" : self.ua.random,
            "Referer" : str(random.choice(REFER_LIST)),
            "Host" : "blog.csdn.net",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close",      # 连接中断
        }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server={}'.format(self.proxy))
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def get_proxy(self):
        proxy_html = requests.get('http://{0}:{1}/random'.format(API_HOST, API_PORT))
        proxy = BeautifulSoup(proxy_html.text, "lxml").get_text()
        print("proxy: ", proxy)
        proxies = {'http': proxy}
        return proxies

    # 请求相应URL,并返回HTML文档
    def parse_url(self, url):
        # 请求前睡眠2秒
        self.wait_time = random.randint(3, 6)
        time.sleep(self.wait_time)
        response = requests.get(url, headers=self.headers, proxies=self.proxy, timeout=3)
        if response.status_code != 200:
            self.get_proxy()
            print('parsing not success!--', self.proxy, url)
            return self.parse_url(url)
        else:
            print('parsing success!--', self.proxy, url, self.wait_time)
            return response.text

    def parse_index(self, html):
        article_urls = []
        soup = BeautifulSoup(html, 'lxml')
        divs = soup.select("div.article-item-box")
        for div in divs[1:]:
            temp_read_num = div.select("div > p:nth-of-type(2) > span")[0].get_text()
            read_num = int(temp_read_num.split("：")[-1])
            if read_num <= READ_NUM:
                article_url = div.select("h4 > a")[0].attrs['href']
                print(article_url, "加入请求队列", read_num)
                article_urls.append(article_url)
        print("本次总任务数：", TASK_NUM)
        while self.task_num <= TASK_NUM:
            # 任务编号
            print("Task ", self.task_num)
            # 更新代理
            self.proxy = self.get_proxy()
            # 更新User-Agent
            self.headers["User-Agent"] = self.ua.random
            # 设置异步IO接口，并分配相应的任务
            loop = asyncio.get_event_loop()
            tasks = [self.request_page(article_url) for article_url in article_urls]
            loop.run_until_complete(asyncio.wait(tasks))
            self.task_num += 1
            print("Task {0} is completed! There are {1} tasks left".format(self.task_num, TASK_NUM-self.task_num))

    async def request_page(self, url):
        html = self.parse_url(url)
        self.browser.get(url)
        self.browser.implicitly_wait(self.wait_time)

    # 逻辑实现
    def run(self):
        html = self.parse_url(self.url)
        self.parse_index(html)

if __name__ == '__main__':
    spider = MyCsdn()
    run_process = Process(target=spider.run)
    run_process.start()