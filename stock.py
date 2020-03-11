import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

def get_code(df, name):
    code = df.query("name=='{}'".format(name))['code'].to_string(index=False)

    return code.strip()

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]

code_df = code_df[['회사명', '종목코드']]

code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

code_df.code = code_df.code.map('{:06d}'.format)

code = get_code(code_df, '삼성전자')

code = code+'.KS'

df = pdr.get_data_yahoo(code, datetime(2020,1,1), datetime(2020,3,11))

print(type(df))
print(df)