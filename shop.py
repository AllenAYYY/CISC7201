# -*- encoding: utf-8 -*-
"""

@File    :   shop.py  
@Modify Time : 2023/11/1 21:33 
@Author  :  Allen.Yang  
@Contact :   MC36514@um.edu.mo        
@Description  : 用来处理shop界面相关功能

"""
from selenium.common import WebDriverException
#import
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import base64
import csv
import time

from selenium.webdriver.support.wait import WebDriverWait

import driver
import ddddocr



#设定好的常量
#登陆的用户名和密码
USERNAME = "mc36514@um.edu.mo"
PASSWD = "mc36514"
#结算清单内容
ADDRESS = "University of Macau W32"
CITY = "Zhuhai"
POSTAL = "519031"
COUNTRY = "China"
URL_HOME = "http://10.113.178.219/"
DIC = {'3rd Generation red OPPO Watch Redmi Note headsets': 0,'5G 3rd Generation 2nd Generation cell Phones&smartphones Internation Version': 1, '64GB 3rd Generation cell Phones&smartphones Internation Version Plus': 2, 'AirTag': 3, 'Airpods Wireless Bluetooth Headphones': 4, 'Amazfit GTR 4': 5, 'Amazfit GTR 4 Pro': 6, 'Amazfit GTS 4 Mini': 7, 'Amazon Echo Dot 3rd Generation': 8, 'Anchor Europe WorldWide Butterfly Silver Metal': 9, 'Anchor Monogram Asia Silver Metal Flower': 10, 'Anchor Roman emperor Monogram Silver Metal Dog': 11, 'Apple 256GB Redmi Note 64GB Plus': 12, 'Apple AirPods Max': 13, 'Apple Internation Version Redmi Note Pro 64GB': 14, 'Apple MacBook Air 11 inches MD223LLA 4GB RAM, 64GB HD, macOS 10.13': 15, 'Apple Pencil 2nd Gen': 16, 'Apple Pencil 2nd Generation': 17, 'Apple TV 4K': 18, 'Apple Watch Series 5': 19, 'Apple Watch Series 8': 20, 'Art Silver Metal - Sealing Wax Europe': 21, 'Art Style Dog Pear Anchor': 22, 'Asia Roman emperor Art Anchor Handle': 23, 'Asia Used wonderful United States Silver Metal': 24, 'BBQ': 25, 'Butterfly Sealing Wax Dog Asia Europe': 26, 'Butterfly Wood WorldWide Asia Monogram': 27, 'Butterfly WorldWide Anchor Style Vintage': 28, 'Cannon EOS 80D DSLR Camera': 29, 'Chinese Anchor Italian Sealing Wax Asia': 30, 'Citizen CZ Smart': 31, 'Coros Apex 2 Pro': 32, 'Coros Pace 2': 33, 'Dog Letters Monogram Anchor United States': 34, 'Echo 3rd Generation Redmi Note 64GB Silver': 35, 'Echo Apple Amazon Plus 5G': 36, 'Echo Internation Version Gold 64GB purple': 37, 'Echo purple Amazon 64GB 128GB': 38, 'Europe Asia Anchor Wood Sealing Wax': 39, 'Europe Wood Art United States Italian': 40, 'Europe wonderful Vintage Pear Italian': 41, 'Fitbit Charge 5 Advanced Health & Fitness Edition': 42, 'Fitbit Inspire 3': 43, 'Flower Asia Wood Anchor Italian': 44, 'Flower Italian Asia Style Monogram': 45, 'Flower Wood Asia Europe Art': 46, 'Fossil Gen 7': 47, 'Fossil Sport': 48, 'French Asia Chinese wonderful Dog': 49, 'Garmin Fenix 7X Solar': 50, 'Garmin Venu 2 Plus': 51, 'Garmin Venu Sq 2': 52, 'Garmin Vivosmart 5': 53, 'Gold 2nd Generation Internation Version 128GB Redmi Note': 54, 'Gold Amazon OPPO Watch Plus headsets': 55, 'Gold Redmi Note Pro Silver Amazon': 56, 'HomePod mini': 57, 'Huawei FreeBuds 5i': 58, 'Huawei FreeBuds Lipstick': 59, 'Huawei FreeBuds Pro': 60, 'Huawei FreeBuds Pro 2': 61, 'Huawei Mate 20X': 62, 'Huawei Mate 60 Pro': 63, 'Huawei MateBook 13s': 64, 'Huawei MateBook 14s': 65, 'Huawei MateBook D 14': 66, 'Huawei MateBook D 15': 67, 'Huawei MateBook E': 68, 'Huawei MateBook X Pro': 69, 'Huawei MatePad Pro 12.6': 70, 'Huawei MatePad SE 10.4': 71, 'Huawei MateStation S': 72, 'Huawei MateStation X': 73, 'Huawei Nova 11 Pro': 74, 'Huawei Nova 9 SE': 75, 'Huawei P40 Pro': 76, 'Huawei P50 Pro': 77, 'Huawei P60 Pro': 78, 'Huawei Sound X': 79, 'Huawei Watch Fit 2': 80, 'Huawei Watch GT 3': 81, 'Huawei Watch GT 3 Elegant': 82, 'Huawei Watch GT 3 Pro': 84, 'Huawei Watch GT 3 Pro Ceramic': 85, 'Huawei Watch GT 3 SE': 86, 'Huawei Watch GT Runner': 88, 'Huawei WiFi AX3': 89, 'Huawei WiFi AX6 Pro': 90, 'Huawei WiFi Mesh 3': 91, 'Huawei WiFi Mesh 7': 92, 'Internation Version 256GB Smart Watches purple 2nd Generation': 93, 'Italian - Handle Monogram Europe': 94, 'Italian Letters Dog Butterfly Silver Metal': 95, 'Italian Wax Stamp WorldWide Rose Used': 96, 'Italian Wood Used Letters wonderful': 97, 'Jitterbug Flip2 Cell Phone for Seniors Red': 98, 'Logitech G-Series Gaming Mouse': 99, 'Mac Pro': 100, 'Mac Studio': 101, 'Mac mini': 102, 'MacBook Air M2': 103, 'MagSafe Battery Pack': 104, 'Magic Keyboard for iPad Pro 12.9-inch': 105, 'Magic Keyboard with Numeric Keypad': 106, 'Magic Trackpad 2': 107, 'Mobvoi TicWatch E3': 108, 'Mobvoi TicWatch E3 Essential': 109, 'Mobvoi TicWatch Pro 3': 110, 'Monogram Italian Handle Wax Stamp Chinese': 111, 'Monogram Vintage - Roman emperor Used': 112, 'Montblanc Summit 3': 113, 'OPPO BDP-103 Universal Disc Player SACD DVD-Audio 3D Blu-ray': 114, 'Oppo A74 Dual-SIM 128GB ROM 6GB RAM GSM Only | No CDMA': 115, 'Pear Roman emperor French Handle Letters': 116, 'Pear Style Wax Stamp Anchor Roman emperor': 117, 'Plus 128GB Echo Amazon Smart Watches': 118, 'Plus 3rd Generation Amazon OPPO Watch Xiaomi': 119, 'Plus accessories green OPPO Watch Amazon': 120, 'Plus purple OPPO Watch Redmi Note Silver': 121, 'Polar Ignite 3': 122, 'Polar Vantage V2': 123, 'Pro Display XDR': 124, 'Pro cell Phones&smartphones Echo purple OPPO Watch': 125, 'Pro cell Phones&smartphones green accessories purple': 126, 'Pro green Xiaomi Apple headsets': 127, 'Redmi Note 128GB Apple red accessories': 128, 'Redmi Note 2nd Generation green headsets 3rd Generation': 129, 'Redmi Note Amazon 5G purple 64GB': 130, 'Redmi Note Internation Version headsets 128GB Amazon': 131, 'Roman emperor Chinese Style Used Wood': 132, 'Roman emperor Chinese Vintage Monogram Europe': 133, 'Roman emperor Wood Style Butterfly Silver Metal': 134, 'Roman emperor wonderful Monogram Anchor Used': 135, 'Samsung Galaxy Watch 5 Pro': 136, 'Samsung Galaxy Watch Active 3': 137, 'Silver Metal Handle - Pear Wax Stamp': 138, 'Silver Metal Wax Stamp Letters Dog WorldWide': 139, 'Silver Redmi Note Internation Version accessories 3rd Generation': 140, 'Silver red Apple Amazon Internation Version': 141, 'Skagen Falster 6': 142, 'Smart Keyboard Folio for iPad Air 5th Gen': 143, 'Smart Watches Xiaomi 64GB purple 3rd Generation': 144, 'Smart Watches headsets Pro green 2nd Generation': 145, 'Smart Watches headsets Redmi Note green Amazon': 146, 'Sony Playstation 4 Pro White Version': 147, 'Studio Display': 148, 'Style Pear Dog Butterfly -': 149, 'Style WorldWide wonderful Silver Metal 19th centery': 150, 'Supershieldz Designed for Samsung Galaxy S20 FE 5G': 151, 'Suunto 5 Peak': 152, 'Suunto 9 Peak Pro': 153, 'TAG Heuer Connected Calibre E4': 154, 'United States Anchor Pear Silver Metal -': 155, 'United States Letters Handle Europe Sealing Wax': 156, 'United States Sealing Wax 19th centery Dog Art': 157, 'Used wonderful Roman emperor Vintage -': 158, 'Vintage Used United States - Sealing Wax': 159, 'Water of joy for fat boys': 160, 'Wood Monogram Flower Art Sealing Wax': 161, 'WorldWide French wonderful Rose Sealing Wax': 162, 'WorldWide Italian Wax Stamp - Vintage': 163, 'WorldWide Sealing Wax Letters 19th centery -': 164, 'Xiaomi 256GB Gold Plus Redmi Note': 165, 'Xiaomi red Smart Watches Amazon 5G': 166, 'accessories 5G Xiaomi cell Phones&smartphones Silver': 167, 'iMac 24-inch': 168, 'iPad Air 5th Gen': 169, 'iPhone 11 Pro 256GB Memory': 170, 'iPhone 14 Pro Max': 171, 'purple 256GB red Smart Watches Redmi Note': 172, 'wonderful - Asia Roman emperor WorldWide': 173, 'wonderful Roman emperor Europe Letters Wax Stamp': 174, '- 19th centery Flower Art Roman emperor': 175, '- Art Asia Roman emperor Used': 176, '- WorldWide Roman emperor Wax Stamp Vintage': 177, '128GB OPPO Watch Plus 5G Pro': 178, '19th centery Style Wax Stamp Used Butterfly': 179, '2021 Apple TV 4K 32GB': 180, '256GB 5G Redmi Note red 2nd Generation': 181, '256GB Pro 5G purple Internation Version': 182, '2nd Generation 64GB red OPPO Watch 3rd Generation': 183, '3rd Generation 2nd Generation red headsets Gold': 184, '3rd Generation 5G 64GB Plus accessories': 185, '3rd Generation Gold 128GB cell Phones&smartphones Apple': 186}

def isclickable(button):
    """
    :description: 判断按钮是否可以点击
    :param button: 按钮元素
    :return: 是否可以点击
    """
    try:
        if button.is_enabled():
            print("按钮可以点击")
        else:
            print("按钮不可点击")
        return True
    except:
        return False

def login(driver,username,psd):
    """
    :description: 登录
    :param driver: 挂载好的驱动
    :param username: 用户名
    :param psd: 密码
    :return: driver
    """

    xpath_login = "//nav[@class='navbar navbar-expand-lg navbar-dark bg-dark']//div[@class='ml-auto navbar-nav']//a[text()=' Sign In']"
    login_need = login_judge(driver,xpath_login)
    #判断是否需要登录
    if login_need:
        login_link = driver.find_element(By.XPATH, xpath_login)
        href_value = login_link.get_attribute("href")
        driver.get(href_value)
        try:
            #准备登录信息
            username_field = driver.find_element(By.XPATH, "//input[@type='email']")
            username_field.send_keys(USERNAME)
            password_feild = driver.find_element(By.XPATH, "//input[@type='password']")
            password_feild.send_keys(PASSWD)
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Sign In']")
            #判断按钮是否可以点击
            is_clicked = isclickable(submit_button)
            if is_clicked:
                driver.implicitly_wait(10)
                submit_button.click()
        except WebDriverException as e:
            print("登录过程发生异常：", e)
        print("完成登录!")
        return driver
    else:
        return driver


def login_judge(driver,xpath_login):
    """
    :description: 判断是否需要登陆
    :param driver: driver
    :param xpath_login: login的超链接搜索路径
    :return: 是否需要登录
    """

    element = driver.find_element(By.XPATH,xpath_login)
    if element:
        print("尚未登录，需要登陆")
        return True
    else:
        print("您已登录，无需再次登陆")
        return False

def search(driver,keyword = "Airpods Wireless Bluetooth Headphones"):
    '''
    :description: 搜索框根据关键字搜索
    :param driver: 挂载driver
    :param keyword: 关键字
    :return: driver
    '''
    search_box = driver.find_element(By.XPATH, "//input[@name='q']")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    first_link = driver.find_element(By.XPATH, "// *[ @ id = 'root'] / main / div / div / div / div / a")
    href_value = first_link.get_attribute("href")
    driver.get(href_value)
    #time.sleep(2)
    return driver

def add_to_car(driver):
    '''
    :description: 添加到购物车
    :param driver: 挂载driver
    :return: driver
    '''
    item = driver.find_element(By.XPATH, "//*[@id='root']/main/div/div[1]/div[3]/div/div/div[2]/div")
    print(item.text)
    if "In Stock" in item.text:
        print("该商品尚有存货可以售出")
        button_car = driver.find_element(By.XPATH, "// *[ @ id = 'root'] / main / div / div[1] / div[3] / div / div / div[4] / button")
        driver.implicitly_wait(10)
        button_car.click()
        driver.get(URL_HOME)
    else:
        print("该商品目前没有存货")
    return driver

def check(driver):
    '''
    :description: 清空购物车
    :param driver: 挂载driver
    :return: driver
    '''
    car_link = driver.find_element(By.XPATH,"//*[@id='basic-navbar-nav']/div/a").get_attribute("href")
    driver.get(car_link)
    button_check = driver.find_element(By.XPATH, "//*[@id='root']/main/div/div/div[2]/div/div/div[2]/button")
    is_clicked = isclickable(button_check)
    if(is_clicked):
        print("进入结算页面")
        driver.implicitly_wait(10)
        button_check.click()

        #结算清单
        address_field = driver.find_element(By.XPATH, "//*[@id='address']")
        address_field.send_keys(ADDRESS)
        city_field = driver.find_element(By.XPATH, "//*[@id='city']")
        city_field.send_keys(CITY)
        postal_field = driver.find_element(By.XPATH, "//*[@id='postalCode']")
        postal_field.send_keys(POSTAL)
        country_field = driver.find_element(By.XPATH, "//*[@id='country']")
        country_field.send_keys(COUNTRY)

        button_submit = driver.find_element(By.XPATH, "// *[ @ id = 'root'] / main / div / div / div / div / form / button")
        submit_clicked = isclickable(button_submit)
        if(submit_clicked):
            print("可以提交清单")
            button_submit.click()
            button_continue = driver.find_element(By.XPATH, "// *[ @ id = 'root'] / main / div / div / div / div / form / button")
            button_continue.click()
            button_place_order = driver.find_element(By.XPATH, "// *[ @ id = 'root'] / main / div / div[2] / div[2] / div / div / div[7] / button")
            button_place_order.click()
            deal_ocr(driver)
        else:
            print("清单无法提交")

    return driver

def deal_ocr(driver):
    '''
    :description: 处理验证码
    :param driver: 挂载driver
    :return: 挂载driver
    '''
    ocr = ddddocr.DdddOcr()
    driver.maximize_window()
    #该图片信息通过canv加载
    canvas = driver.find_element(By.XPATH,"//*[@id='canv']")
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    # 将 base64 编码的图片数据转换为二进制数据
    image_data = base64.b64decode(canvas_base64)
    # 保存图片到本地文件
    with open("./code.png", "wb") as file:
        file.write(image_data)
    with open("./code.png", "rb") as f:
        img_bytes = f.read()
    ocr_result = ocr.classification(img_bytes)
    print(f"已识别验证码，验证码为:{ocr_result}")
    ocr_field = driver.find_element(By.XPATH, "// *[ @ id = 'user_captcha_input']")
    ocr_field.send_keys(ocr_result)
    button_submit = driver.find_element(By.XPATH,"// *[ @ id = 'root'] / main / div / div / div[2] / div / div / div[6] / div / div / div / div[3] / div / button")
    button_submit.click()

def find_k_x_expensive(driver,keyword="Play",x=3):
    '''
    :description: 找出关键字为keyword，最贵的x个产品
    :param driver: 挂载driver
    :param keyword: 关键字
    :param x: x个
    :return: 商品列表，形如[{name:'xx',price:'xx',description:'xx'},{name:'yy',price:'yy',description:'yy'}]
    '''
    def description_get(products):
        '''
        :description: 将原商品列表中的URL替换成description
        :param products: 商品列表
        :return: products-替换成描述信息后的商品列表
        '''
        for item in products:
            driver.get(item['url'])
            description = driver.find_element(By.XPATH,"//*[@id='root']/main/div/div[1]/div[2]/div/div[4]").text
            print(description)
            description = description[len("Description:"):]
            del item['url']
            item['description'] = description

        print(f"商品清单为：{products}")
        return products

    def next_page(driver):
        """
        :description: 查找下一页
        :param driver:
        :return:
        """
        break_flag = 0
        # 查找包含页数的元素
        #wait = WebDriverWait(driver, 10)
        #pagination = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/main/div/ul")))
        pagination = driver.find_elements(By.CLASS_NAME, "pagination")
        #不存多页的情况
        if(len(pagination)<=0):
            return driver,1
        # 查找当前页的元素
        #print(pagination[0].get_attribute())
        current_page = pagination[0].find_element(By.XPATH,".//li[contains(@class, 'active')]/span")
        #当前页面的链接.find_element(By.XPATH,"./span")
        current_page_url = current_page.get_attribute("href")
        current_page_url_deal = current_page_url.rpartition("/")[0] + "/"
        print(f"当前网址：{current_page_url}")
        print(current_page.text.split("(")[0])
        # 获取当前页数
        current_page_number = int(current_page.text.split("(")[0])
        xpath = "//a[@href='"+current_page_url_deal+ str(current_page_number+1) + "']"
        # 查找下一页的元素
        next_page = pagination[0].find_elements(By.XPATH,
            xpath)
        # 判断是否存在下一页
        if len(next_page)>0:
            # 点击下一页的链接
            # print(f"下一页的链接:{next_page}")
            driver.get(next_page[0].get_attribute("href"))
        else:
            break_flag = 1
        return driver,break_flag

    #url_home = driver.find_element(By.XPATH, "// *[ @ id = 'root'] / header / nav / div / a").get_attribute("href")
    driver.get(URL_HOME)
    search_field = driver.find_element(By.XPATH, "// *[ @ id = 'basic-navbar-nav'] / form / input")
    search_field.send_keys(keyword)
    button_search = driver.find_element(By.XPATH, "//*[@id='basic-navbar-nav']/form/button")
    button_search.click()
    products = []
    break_flag = 1
    while True:
        product_items = driver.find_elements(By.XPATH,"// *[ @ id = 'root'] / main / div / div/div")
        for product in product_items:
            name_filed = product.find_element(By.XPATH,".//div[@class='card-title']").text
            price_field = product.find_element(By.XPATH,".//h3[@class='card-text']").text
            url_field = product.find_element(By.XPATH,".//a").get_attribute("href")
            products.append({"name":name_filed,"price":price_field,"url":url_field})

        driver,break_flag = next_page(driver)
        if break_flag == 1:
            break
    if(len(products)>0):
        products = sorted(products,key=lambda p: float(p['price'].lstrip('$')), reverse=True)[:x]
    result = description_get(products)
    csv_file = './products.csv'
    # 指定 CSV 文件的列名
    fieldnames = ['name', 'price', 'description']
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # 写入列名
        writer.writeheader()
        # 写入数据
        writer.writerows(result)
    print(f"文件存放在{csv_file}.")
    driver.get(URL_HOME)
    return result



def process_task1(driver,keyword = "Sony Playstation 4 Pro White Version"):
    '''
    :description: 完成登录->进入商品页面->商品添加到购物车->继续结账->填写信息->下单->填写验证码 过程
    :param driver: 挂载的driver
    :param keywrod: 搜索的关键字,默认为Sony Playstation 4 Pro White Version
    :return: driver
    '''
    driver = login(driver, USERNAME, PASSWD)
    name = input("请输入关键字：") or keyword
    driver = search(driver, name)
    driver = add_to_car(driver)
    driver = check(driver)
    driver.get(URL_HOME)
    return driver

def process_task2(driver,keyword="Play",x=3):
    '''
    :description: 完成根据关键字查找前x个最贵商品，根据价格高低存放到CSV文件
    :param driver: 挂载的driver
    :param keyword: 查找的关键字 默认为”Play“
    :param x: 最贵的x个商品  默认为3
    :return: 商品列表，形如[{name:'xx',price:'xx',description:'xx'},{name:'yy',price:'yy',description:'yy'}]
    '''
    #driver = login(driver, USERNAME, PASSWD)
    name = input("请输入关键字：") or keyword
    number = int(input("请输入数量：")) or x
    result = find_k_x_expensive(driver,name,number)
    driver.get(URL_HOME)
    return result

def process_task3(driver,products_list):
    """
    :description: 接着task2，将task2查找到的最贵的x件商品下单
    :param driver: 挂载的driver
    :param products_list: 商品列表
    :return: driver
    """
    if(len(products_list)==0):
        return
    #driver = login(driver,USERNAME,PASSWD)
    for product in products_list:
        driver = search(driver,product['name'])
        add_to_car(driver)
    time.sleep(3)
    check(driver)
    driver.get(URL_HOME)
    return driver

def process_task4(driver,keyword="GPS"):
    '''
    :description: 完成从商品描述中扫描包含关键字的商品并下单
    :param driver: 挂载driver
    :param keyword: 关键字
    :return: none
    '''
    flag = 0
    page_links = driver.find_elements(By.XPATH,"//*[@id='root']/main/div/ul/li/a")
    wait = WebDriverWait(driver, 10)
    links = []
    for page in page_links:
        link = page.get_attribute("href")
        links.append(link)
    links.sort(reverse=True)
    while(flag == 0):
        for page_link in links:
            print(page_link)
            products = []
            driver.get(page_link)
            break_flag = 0
            product_links = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/main/div/div[2]")))
            #wait = WebDriverWait(driver, 10)
            #product_links = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='product_links']")))
            product_name = product_links.find_elements(By.XPATH, "./div/div/div/a/div")
            for name in product_name:
                if name.text in DIC:
                    continue
                else:
                    break_flag = 1
                    break
            if(break_flag == 0):
                continue
            product_links = product_links.find_elements(By.XPATH, "./div/div/a")
            for i in product_links:
                j = i.get_attribute("href")
                products.append(j)
            for item in products:
                driver.get(item)
                elements = driver.find_element(By.XPATH,
                                               "// *[ @ id = 'root'] / main / div / div[1] / div[2] / div / div[4]").text
                if (keyword in elements):
                    flag = 1
                    driver = add_to_car(driver)
                    check(driver)
                    break
            if (flag == 1):
                break
        if(flag == 0):
            print("商品未更新！")



if __name__ == '__main__':
    driver = driver.diriver_build()
    driver = login(driver,USERNAME,PASSWD)
    #driver = process_task1(driver)
    #results = process_task2(driver)
    #driver = process_task3(driver,results)
    process_task4(driver,"CISC7201")
    #process_task4(driver, "knell")




