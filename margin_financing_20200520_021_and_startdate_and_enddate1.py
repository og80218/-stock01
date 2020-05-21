#上櫃融資融券爬蟲寫入mysql

import requests, pprint
from bs4 import BeautifulSoup
import json
import MySQLdb
from datetime import datetime
import time
import random
import re
import startdate_and_enddate1      #去抓startdate_and_enddate1.py => 設定抓取資料的起始日及結束日
import stockid

# 取得所有股票代碼
tmp_list = stockid.Stockiid.values()
stock_iids = []
for i in tmp_list:
    i = i.replace(' ', '')
    stock_iids.append(i)

# 連接我的資料庫
db = MySQLdb.connect(host='localhost', user='dbuser', passwd='aabb1234', db='project_test', port=3306, charset='utf8')

cursor = db.cursor()
db.autocommit(True)

T = (startdate_and_enddate1.create_assist_date('2020-05-20'))  #設定抓取資料的起始日及結束日的變數
T = [startdate_and_enddate1.turnyear(t) for t in T]            #強制西元改民國
# print(T)
for t in T:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    url = "https://www.tpex.org.tw/web/stock/margin_trading/margin_balance/margin_bal_result.php?l=zh-tw&o=json&d={}&_=1589967569195".format(t) #融資融券
    res = requests.get(url, headers=headers)
    # print(res)

    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)

    jdata = json.loads(res.text, encoding='utf-8')
    # print(type(jdata))

    for i in jdata['aaData']:
        # print(list(abc))
        # print(jdata['reportDate'])
        ddd = jdata['reportDate']
        eee = list(ddd)
        # print(eee)
        g1 = eee[0]
        g2 = eee[1]
        g3 = eee[2]
        g4 = eee[4]
        g5 = eee[5]
        g6 = eee[7]
        g7 = eee[8]
        g = g1 + g2 + g3 + g4 + g5 + g6 + g7
        f = int(g) + 19110000
        # print(f)

        ee = datetime.strptime(str(f), '%Y%m%d').strftime('%Y-%m-%d')
        # print(ee)       #已成功由105/05/05轉成2016-05-05

        abc = [ee, i[0], i[3], i[4], i[6], i[9], i[11], i[12], i[14], i[17]]
        # 將網站爬下的數值，有逗號部分刪除
        abc[2] = (abc[2].replace(',', ''))
        abc[3] = (abc[3].replace(',', ''))
        abc[4] = (abc[4].replace(',', ''))
        abc[5] = (abc[5].replace(',', ''))
        abc[6] = (abc[6].replace(',', ''))
        abc[7] = (abc[7].replace(',', ''))
        abc[8] = (abc[8].replace(',', ''))
        abc[9] = (abc[9].replace(',', ''))


        print(abc)

        # g = []
        # g.append(jdata['reportDate'])         #OK-民國日期
        # g.append(jdata['aaData'][0][0])       #OK-股票代碼
        # g.append(jdata['aaData'][0][3])       #融資買進
        # g.append(jdata['aaData'][0][4])       #融資賣出
        # g.append(jdata['aaData'][0][6])       #融資餘額
        # g.append(jdata['aaData'][0][9])       #融資限額
        # g.append(jdata['aaData'][0][11])      #融券買進
        # g.append(jdata['aaData'][0][12])      #融券賣出
        # g.append(jdata['aaData'][0][14])      #融券餘額
        # g.append(jdata['aaData'][0][17])      #融券限額
        # print(g)
#
#     # OK
        
        try:
            if i[0] in stock_iids:
                cursor.execute('INSERT INTO margin_trading_short_selling(date, stockiid, margin_buy, margin_cell, '
                               'margin_remaining, margin_limit, short_buy, short_cell, '
                               'short_remaining, short_limit)' \
                               '' 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', abc)

        except Exception as err:
            print(err.args)
    sleep_time = random.randint(15, 30) + random.random()
    time.sleep(sleep_time)
# # db.commit()
# # cursor.close()
print('Done')
