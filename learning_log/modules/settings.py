'''本模块定义常用变量'''

import traceback
import datetime as dt

DATA_FILE = 'data/data.json'
JSON_FILE = 'data/data.json'
CSV_FILE = 'data/data.csv'
ERROR_FILE = 'data/error_log.txt'
CACHE_FILE = 'data/data_cache'
USED_CSV_FILE = 'data/used_data.csv'

TYPE = 0
YEAR = 1
MONTH = 2
DAY = 3
TIMES = 4
QUESTION = 5
SA = 6
SB = 7
SC = 8
SD = 9
ANSWER = 10

DELTA_DAYS = [0, 1, 2, 7, 15, 30, 365, 1000]
NUMBER_OF_ELEMENTS = 11

def log_error(info, line=None):
    with open(ERROR_FILE, 'a') as ef:
        print(dt.datetime.now(), file=ef)
        traceback.print_exception(*info, file=ef)
        if line:
            print("# Error is in line of data:", line, file=ef)
        print(file=ef)