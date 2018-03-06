'''本程序检查今天应复习的题'''

import json
import datetime as dt
import sys
import os

from settings import *

def review():
    '''检查今天要复习的题目'''
    # 获取题目并将其存入内存
    contents = []
    try:
        with open(DATA_FILE) as df:
            contents = json.load(df)
    except FileNotFoundError:
        log_error(sys.exc_info())
        print("数据库不存在")
        os.system("pause")
        return
        
    today = dt.date.today()
    
    i = 0
    for content in contents:
        i += 1
        
        # 加载日期，如果复习次数超标则跳过
        input_date = dt.date(content['year'], content['month'], content['day'])
        try:
            due_date = input_date + dt.timedelta(
                days=DELTA_DAYS[content['times']])
        except IndexError:
            log_error(sys.exc_info(), line=i)
            print("第%i复习次数有误，请更新数据" % i)
            os.system("pause")
            continue
            
        if due_date <= today:
            # 展示问题，并根据回答正误更新数据库
            flag = show_question(content)
            if flag:
                content['times'] += 1
            else:
                content['times'] = 0
                content['year'] = today.year
                content['month'] = today.month
                content['day'] = today.day
            update_data(contents)
            
    print("\n今日任务已完成！")
    os.system("pause")
    
def update_data(contents):
    # 写入缓存文件，然后删除原文件，最后把缓存文件重命名
    with open(CACHE_FILE, 'w') as dc:
        json.dump(contents, dc)
    try:
        os.remove(DATA_FILE)
    except FileNotFoundError:
        pass
    os.rename(CACHE_FILE, DATA_FILE)
    
def show_question(content):
    # 显示题目，获取输入答案
    os.system("CLS")
    print("题目类型：" + content['type'])
    print(content['question'])
    print("A. " + content['sa'])
    print("B. " + content['sb'])
    print("C. " + content['sc'])
    print("D. " + content['sd'])
    answer = input("请作答：").strip().lower()
    
    # 根据作答正误显示提示，并返回结果
    if answer == content['answer']:
        print("\n回答正确！")
        print("正确答案是", content['answer'].upper())
        os.system("pause")
        return True
    else:
        print("\n回答错误！")
        print("正确答案是", content['answer'].upper())
        print("本题的复习计划将从头计算")
        os.system("pause")
        return False
        