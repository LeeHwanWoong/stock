#-*- coding: utf-8 -*-
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime
import openpyxl

def get_code(df, name):
    code = df.query("name=='{}'".format(name))['code'].to_string(index=False)

    return code.strip()

def get_name(df, code):
    name = df.query("code=='{}'".format(code))['name'].to_string(index=False)

    return name

f = open("kosdaq_code.txt", 'r')
codes = f.read().split()
f.close()

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]

code_df = code_df[['회사명', '종목코드']]

code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

code_df.code = code_df.code.map('{:06d}'.format)

for code in codes:
    name=get_name(code_df, code)
    try:
        data = pdr.get_data_yahoo(code+'.kq', datetime(2020,3,13), datetime(2020,3,13))
        print(name+","+code+","+str(data.values[0][3]))
    except Exception as ex:
        pass