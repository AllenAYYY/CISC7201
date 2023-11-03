# -*- encoding: utf-8 -*-
"""

@File    :   driver.py  
@Modify Time : 2023/11/1 21:23 
@Author  :  Allen.Yang  
@Contact :   MC36514@um.edu.mo        
@Description  : 完成googledriver的挂载

"""
#import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#driver路径
webdriver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
#shop网址
url_shop_home = 'http://10.113.178.219'


def diriver_build():

    #添加部分参数以绕过google自动检测
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("disable-infobars")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--start-maximized")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument("window-size=1280,800")
    options.add_experimental_option("detach", True)

    #采用service的方式构建driver
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url_shop_home)
    driver.maximize_window()
    return driver


if __name__ == '__main__':
    driver = diriver_build()
    print(driver)
