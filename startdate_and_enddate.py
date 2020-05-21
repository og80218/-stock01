#給予起始時間及結束時間

import datetime
def create_assist_date(datestart=None, dateend=None):
    if datestart is None:
        datestart = '20161003'      #輸入起始西元年月份
    if dateend is None:
        dateend = datetime.datetime.now().strftime( '20161004' )        #輸入結束西元年月份

    datestart = datetime.datetime.strptime( datestart, '%Y%m%d' )
    dateend = datetime.datetime.strptime( dateend, '%Y%m%d' )
    date_list = []
    date_list.append( datestart.strftime( '%Y%m%d' ) )
    while datestart < dateend:
        datestart += datetime.timedelta( days=+1 )
        date_list.append( datestart.strftime( '%Y%m%d' ) )
    return date_list
