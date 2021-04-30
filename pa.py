import requests
import pandas as pd
import numpy as np
import os
import pymysql


def to_date(s):  # 将年-月-日转化为时间戳
    # print(s)
    y, m, d = s.split("-")
    date = datetime.date(int(y), int(m), int(d))
    return date


def read_file():
    res = []
    current_path = os.path.dirname(__file__)  # 获取当前文件的path
    names = pd.read_csv(current_path + 'names.csv')  # 此处如果本地运行需要写成 current_path+'\\names.csv'格式   读文件
    for x in names['name']:  # 遍历文件内容
        res.append(x)  # 存储到列表中
    return res


def write_file(titles):
    a = np.array(titles).reshape((len(titles), 1))  # 转置
    df = pd.DataFrame(a)  # 创建一张数据表
    df.columns = ['title']  # 设置数据表的列索引
    current_path = os.path.dirname(__file__)  # 返回当前路径
    df.to_csv(current_path + '\\titles.csv', encoding='utf_8_sig')  # 将文件写入当前文件路径  设置编码格式为utf_8_sig


def get_news(news, idx):
    try:
        hd = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6)',
              'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
        r = requests.get(news, headers=hd, timeout=1000)  # timeout 限制时间   函数返回html
        r.raise_for_status()  # 判断网络连接是否异常
        r.encoding = r.apparent_encoding  # 从内容中分析出的响应内容编码
    except:
        return {'id': None, 'title': None, 'content': None, 'time': None}  # 出现异常后的输出
