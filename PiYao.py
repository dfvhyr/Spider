from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
import re
import platform
from lxml import etree
from datetime import datetime
#准备工作
header = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
url = r'http://piyao.sina.cn/'
if platform.system()=='Windows':
    chrome_driver_path = "chromedriver.exe"
elif platform.system()=='Linux' or platform.system()=='Darwin':
    chrome_driver_path = "./chromedriver"
else:
    print('Unknown System Type. quit...')

#创建一个Chrome webdriver的实例
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path= chrome_driver_path)

#打开URL中填写的地址，WebDriver将等待,直到页面完全加载完毕，然后返回继续执行脚本
driver.get(url)
#推迟执行的秒数
time.sleep(1)

#重复150次以获取足够的数据，每次都读取到页面最底部
for i in range(150):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
#获得所需的元素    
name=driver.find_elements_by_xpath('//div[@class="left_title"]')
number=driver.find_elements_by_xpath('//div[@class="like_text"]')

#对获得的元素进行处理
High_Names=[]
High_Numbers=[]
for x in name:
    High_Names.append(x.text)
for y in number:
    High_Numbers.append(int(y.text))

names_and_numbers=zip(High_Names,High_Numbers)
high_agreement = sorted(names_and_numbers,key=lambda x : x[1])

print("辟谣新闻点赞数前十名：")
for t in high_agreement[-10:]:
    print( t[0],'\t',t[1])