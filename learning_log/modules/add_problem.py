'''此程序向错题本中添加一个错题'''

import datetime as dt
import json
from collections import OrderedDict
import sys
import os

from settings import *

def add_problem():
    contents = []
    try:
        with open(DATA_FILE) as df:
            contents = json.load(df)
    except FileNotFoundError:
        pass
        
    content = OrderedDict()
    content['type'] = input("请输入法律类型：").strip().replace(',', '，')
    date = dt.date.today()
    content['year'] = date.year
    content['month'] = date.month
    content['day'] = date.day
    content['times'] = 0
    content['question'] = input("\n请输入题干：\n").strip().replace(',', '，')
    content['sa'] = input("\n请输入A选项：\n").strip().replace(',', '，')
    content['sb'] = input("\n请输入B选项：\n").strip().replace(',', '，')
    content['sc'] = input("\n请输入C选项：\n").strip().replace(',', '，')
    content['sd'] = input("\n请输入D选项：\n").strip().replace(',', '，')
    content['answer'] = input("\n请输入正确选项：\n").strip().lower()
    
    contents.append(content)
    with open(CACHE_FILE, 'w') as dc:
        json.dump(contents, dc)
    try:
        os.remove(DATA_FILE)
    except FileNotFoundError:
        pass
    os.rename(CACHE_FILE, DATA_FILE)
    print('题目添加成功')
    os.system('pause')