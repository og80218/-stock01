#給予起始時間及結束時間

import datetime

#西元改民國
def turnyear(A):
    y = str( int( A.split( '-' )[0] ) - 1911 )
    m = A.split( '-' )[1]
    d = A.split( '-' )[2]
    B = y + '/' + m + '/' + d
    return B


def create_assist_date(datestart=None, dateend=None):
    if datestart is None:
        datestart = '2016-10-03'          #輸入起始西元年月份
    if dateend is None:
        dateend = datetime.datetime.now().strftime( '2016-10-04' )          #輸入結束西元年月份

    datestart = datetime.datetime.strptime( datestart, '%Y-%m-%d' )
    dateend = datetime.datetime.strptime( dateend, '%Y-%m-%d' )
    date_list = []
    date_list.append( datestart.strftime( '%Y-%m-%d' ) )
    while datestart < dateend:
        datestart += datetime.timedelta( days=+1 )
        date_list.append( datestart.strftime( '%Y-%m-%d' ) )
    return date_list
