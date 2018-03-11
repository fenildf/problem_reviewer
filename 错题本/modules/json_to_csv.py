import sys
import os
import datetime as dt
import json
from settings import *

def json_to_csv():
    data = []
    try:
        with open(JSON_FILE) as jf:
            data = json.load(jf)
    except FileNotFoundError:
        log_error(sys.exc_info())
        print("json文件不存在")
        os.system("pause")
        return
        
    with open(CSV_FILE, 'w') as cf:
        for content in data:
            for value in content.values():
                cf.write(str(value) + ',')
            cf.write('\n')
            
    print("已输出CSV文件")
    os.system("pause")
