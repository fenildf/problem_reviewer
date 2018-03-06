import os
import sys

sys.path.append('modules')

import add_problem
import review
import json_to_csv
import csv_to_json

active = True
os.system('color 1e')

while active:
    print('请输入要进行的操作：')
    msg = ('(a=添加题目, r=复习错题, q=退出, c=从表格导入题目, ' + 
        'j=从数据库导出至表格) ')
    c = input(msg)
    
    if c == 'a':
        add_problem.add_problem()
    elif c == 'r':
        review.review()
    elif c == 'j':
        json_to_csv.json_to_csv()
    elif c == 'c':
        csv_to_json.csv_to_json()
    elif c == 'q':
        active = False
    else:
        print("输入不合法")
        continue
        
    os.system("cls")