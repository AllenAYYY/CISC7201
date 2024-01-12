# -*- encoding: utf-8 -*-
"""

@File    :   wechat_crawel.py  
@Modify Time : 2023/11/17 16:37 
@Author  :  Allen.Yang  
@Contact :   MC36514@um.edu.mo        
@Description  : 爬取考试宝中题库中的题

"""

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

# 指定driver路径
webdriver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"

# 登陆网址
url = "https://www.zaixiankaoshi.com/login/"

# 构建webDriver对象，主要目的是添加一系列参数来绕过Chrome的自动检测
# 具体添加的参数不固定，根绝情况来添加，但一般按照我这种添加方式都可以
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

    # 采用service的方式构建driver
    # Service是WebDriver的一个组件，负责启动和管理浏览器驱动程序的进程。
    #
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    # get方法访问url网址
    driver.get(url)
    # 最大化窗口
    driver.maximize_window()
    return driver

# 打开考试宝网站
driver = diriver_build()
# 登录账号
# 分别找到用户名的输入框、密码输入框和登录按钮
# 向表单中添加信息一般用send_keys()
# 点击按钮一般是click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/section/div[2]/div/div[2]/form/div/div[1]/div/div/div/input").send_keys("xx")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/section/div[2]/div/div[2]/form/div/div[2]/div/div/div/input").send_keys("xx")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/section/div[2]/div/div[2]/form/div/div[3]/button").click()
time.sleep(1)

# 要爬取的目标编号和开始题号
paperId = 12211729
sequence = 0

# 构造题目页面的URL
url = "https://www.zaixiankaoshi.com/online/?paperId=" + str(paperId) + "&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=" + str(sequence) + "&is_collect=0"

# 在新窗口中打开题目页面(打开新的URL)
js = "window.open('" + url + "');"
driver.execute_script(js)
new_window = driver.window_handles[-1]   # 可能会有多个窗口弹出的情况，选择最后一个窗口的句柄
# 跳转到最后一个窗口
driver.switch_to.window(new_window)

#https://www.zaixiankaoshi.com/online/?paperId=12319433&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=0&is_collect=0
# 循环爬取题目并存储到Markdown文件
x = 0
#checkbox = driver.find_element(By.XPATH, "//*[@id='body']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/p[2]/span[2]/div/input")

# 使用click()方法点击复选框
#checkbox.click()
#checkbox = driver.find_element("css selector", "input.el-switch__input")

# 使用JavaScript来更改复选框的状态//*[@id="body"]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div
#driver.execute_script("arguments[0].click();", checkbox)
#time.sleep(3)
# 打开背题模式，这样可在网页上直接看到正确答案是什么
checkbox = driver.find_element(By.XPATH,'//*[@id="body"]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/p[2]/span[2]/div/input')

# 使用ActionChains模拟鼠标点击操作
# 先移动到对应的元素位置，再点击元素（按钮）
# perform是执行之前的一切操作，执行到perform的时候才会在页面进行鼠标移动、点击按钮这些动作
actions = ActionChains(driver)
actions.move_to_element(checkbox).click().perform()
time.sleep(7)
while True:

    answer = driver.find_element(By.XPATH, "//*[@id='body']/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div")
    options = answer.find_elements(By.CLASS_NAME, "option")
    print(len(options))
    correct_options = answer.find_elements(By.CLASS_NAME, "right")
    print(len(correct_options))

    """correct_options = []
    for option in options:
        if "right" in option.get_attribute("class"):
            correct_options.append(option.text)"""
    type = driver.find_element(By.XPATH, "//*[@id='body']/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div/span[1]").text
    question = driver.find_element(By.XPATH, "//*[@id='body']/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div/div").text
    next = driver.find_element(By.ID,"xx")
    #options = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/section/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div").find_elements(By.CLASS_NAME, "option")
    # 不一定有解析，没解析的时候找不到元素会抛出异常，用try-except捕捉并进行相应的操作
    try:
        explain = driver.find_element(By.CLASS_NAME, "answer-analysis").text
    except:
        explain = ""

    # 构造题目的Markdown格式文本

    markdown_text = f"**题目{x+1}：** {question}\n\n"
    markdown_text += f"**类型：** {type}\n\n"
    for i, option in enumerate(options):
        option_no = option.find_element(By.CLASS_NAME, "before-icon").text
        option_text = option.find_elements(By.TAG_NAME, "span")[1].text

        if option in correct_options:
            markdown_text += f"**选项 {option_no}：** **<span style='color:yellow'>{option_text}</span>**\n\n"
        else:
            markdown_text += f"**选项 {option_no}：** {option_text}\n\n"

    markdown_text += f"**解析：** {explain}\n\n"

    # 将题目的Markdown格式文本写入文件
    with open("questions_2.md", "a", encoding="utf-8") as file:
        file.write(markdown_text)

    x += 1
    print(f"已完成第 {x} 题的读取")
    '''if x==3:
        break'''
    driver.find_element(By.XPATH, "//*[@id='body']/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[3]/button[2]").send_keys(Keys.ENTER)
    if x == 10:
        print("第十题")
        time.sleep(2)
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
    if x % 10 == 0:
        time.sleep(3)