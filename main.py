# -*- encoding: utf-8 -*-
"""

@File    :   main.py
@Modify Time : 2023/11/1 18:25 
@Author  :  Allen.Yang  
@Contact :   MC36514@um.edu.mo        
@Description  :  Main file

"""

#import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from driver import diriver_build
import shop

if __name__ == '__main__':
    driver = diriver_build()
    #keyword_car = "Sony Playstation 4 Pro White Version"
    #shop.process(driver,keyword_car)
    #shop.find_k_x_expensive(driver)