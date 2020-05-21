#20200520_1
#上市融資融券爬蟲寫入mysql
import requests
from bs4 import BeautifulSoup
import json
import MySQLdb
from datetime import datetime
import time
import random
import startdate_and_enddate      #去抓startdate_and_enddate.py => 設定抓取資料的起始日及結束日

# 連接我的資料庫
db = MySQLdb.connect(host='localhost', user='dbuser', passwd='aabb1234', db='project_test', port=3306, charset='utf8')

cursor = db.cursor()
db.autocommit(True)

T = (startdate_and_enddate.create_assist_date())  #設定抓取資料的起始日及結束日的變數

for t in T:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    url = "https://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date={}&selectType=STOCK&_=1589002919516".format(t) #融資融券
    res = requests.get(url, headers=headers)
    # print(res)

    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.text)

    jdata = json.loads(res.text, encoding='utf-8')
    # print(jdata)

    #data資料
    #刪除jdata['data']第一排
    dd = []
    aa = jdata['data']
    for a in aa:
        dd.append(a)
    # print(dd)
    aa = dd[1:]
    # print(aa)
    # print(len(aa)) #看筆數

    for a in aa:
        abc = (t, a[0], a[2], a[3], a[6], a[7], a[8], a[9], a[12], a[13])
        # print(list(abc)) #list顯示
        # print(abc[0])
        date = t
        
        #更改日期模式YYYYMMDD => YYYY-MM-DD
        ddd = datetime.strptime(str(date), '%Y%m%d').strftime('%Y-%m-%d')
        # print(ddd)
        abc = [ddd, a[0], a[2], a[3], a[6], a[7], a[8], a[9], a[12], a[13]]
        
        #將網站爬下的數值，有逗號部分刪除
        abc[2] = (abc[2].replace(',', ''))
        abc[3] = (abc[3].replace(',', ''))
        abc[4] = (abc[4].replace(',', ''))
        abc[5] = (abc[5].replace(',', ''))
        abc[6] = (abc[6].replace(',', ''))
        abc[7] = (abc[7].replace(',', ''))
        abc[8] = (abc[8].replace(',', ''))
        abc[9] = (abc[9].replace(',', ''))
        # print(abc)        #print(abc)可先解註解，下述程式碼可先註解，先完成爬蟲部分，再做寫入mysql部分

    # OK
    #mysql，SELECT * FROM project_test.margin_trading_short_selling;執行完，可點Fetch_rows=>下一頁的意思
         try:
             cursor.execute('INSERT INTO margin_trading_short_selling(date, stockiid, margin_buy, margin_cell, '
                            'margin_remaining, margin_limit, short_buy, short_cell, '
                            'short_remaining, short_limit)' \
                            '' 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', abc)
    
         except Exception as err:
             print(err.args)
#     若遇到索IP，請設定隨機停留時間
#     sleep_time = random.randint(5, 30) + random.random()
#     time.sleep(sleep_time)
# db.commit()
# cursor.close()
    print('Done')
