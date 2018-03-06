import sys
import os
import datetime as dt
import json
from settings import *
from collections import OrderedDict

def csv_to_json():
    data = ''
    try:
        with open(CSV_FILE) as cf:
            data = cf.read()
    except FileNotFoundError:
        log_error(sys.exc_info())
        print("csv文件不存在")
        os.system('pause')
        return
        
    lines = data.rstrip()
    contents = []
    if lines:
        i = 0
        lines = lines.split('\n')
        for line in lines:
            i += 1
            line = line.rstrip(',').split(',')
            try:
                content = OrderedDict()
                content['type'] = line[TYPE]
                content['year'] = int(line[YEAR])
                content['month'] = int(line[MONTH])
                content['day'] = int(line[DAY])
                content['times'] = int(line[TIMES])
                content['question'] = line[QUESTION].replace(',', '，')
                content['sa'] = line[SA].replace(',', '，')
                content['sb'] = line[SB].replace(',', '，')
                content['sc'] = line[SC].replace(',', '，')
                content['sd'] = line[SD].replace(',', '，')
                content['answer'] = line[ANSWER].strip().lower()
            except ValueError:
                log_error(sys.exc_info(), line=i)
                print("第%i行数据有误，如把数字输入成文本" % i)
                os.system('pause')
                return
            except IndexError:
                log_error(sys.exc_info(), line=i)
                print("第%i行数据数量不足" % i)
                os.system('pause')
                return
            else:
                contents.append(content)
                
    with open(CACHE_FILE, 'w') as jc:
        json.dump(contents, jc)
    try:
        os.remove(JSON_FILE)
    except FileNotFoundError:
        pass
    os.rename(CACHE_FILE, JSON_FILE)
    try:
        os.remove(USED_CSV_FILE)
    except FileNotFoundError:
        pass
    os.rename(CSV_FILE, USED_CSV_FILE)
    print("csv文件已导入")
    os.system("pause")
    