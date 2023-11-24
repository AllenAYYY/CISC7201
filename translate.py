# -*- encoding: utf-8 -*-
"""

@File    :   translate.py  
@Modify Time : 2023/11/24 10:44 
@Author  :  Allen.Yang  
@Contact :   MC36514@um.edu.mo        
@Description  : markdown转html

"""
import googletrans
import markdown
from googletrans import Translator

def translate_markdown(input_file, output_file):
    # 初始化Google翻译器
    translator = Translator(service_urls=['translate.google.com'])

    # 打开输入文件和输出文件
    with open(input_file, 'r', encoding='utf-8') as input_file, \
            open(output_file, 'w', encoding='utf-8') as output_file:
        # 读取输入文件中的Markdown文本
        markdown_text = input_file.read()


        # 将Markdown文本解析为HTML
        html = markdown.markdown(markdown_text)
        #html = "<p><strong>题目1：</strong> 反向传播是用来训练人工神经网络的常见方法(AI考点)</p> <p><strong>类型：</strong> 单选题</p> <p><strong>选项 A：</strong> <strong><span style='color:red'>TRUE</span></strong></p> "
        #print(type(html))
        print(html)
        output_file = "output1.html"  # 输出文件名，可以根据需要进行修改
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html)
        # 使用Google翻译器翻译HTML文本
        #translation = translator.translate(html, src='zh-CN', dest='en')
        #print(translation)

        # 将翻译结果写入输出文件
        #output_file.write(str(translation.text))


if __name__ == '__main__':
    input_file = './questions.md'  # 输入Markdown文件路径
    output_file = './questions2_en.md'  # 输出Markdown文件路径

    translate_markdown(input_file, output_file)