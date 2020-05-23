#給予起始時間及結束時間
#給予當天時間
import datetime

#西元改民國
def turnyear(A):
    y = str( int( A[0:4] ) - 1911 )
    m = A[4:6]
    d = A[6:8]
    B = y + '/' + m + '/' + d
    return B

#給予起始時間及結束時間
def create_assist_date(datestart=None, dateend=None):
    if datestart is None:
        datestart = '20161003'
    if dateend is None:
        dateend = datetime.datetime.now().strftime( '20200521' )

    datestart = datetime.datetime.strptime( datestart, '%Y%m%d' )
    dateend = datetime.datetime.strptime( dateend, '%Y%m%d' )
    date_list = []
    date_list.append( datestart.strftime( '%Y%m%d' ) )
    while datestart < dateend:
        datestart += datetime.timedelta( days=+1 )
        date_list.append( datestart.strftime( '%Y%m%d' ) )
    return date_list

#給予當天時間
def create_assist_date_now(datestart=None, dateend=None):
    if datestart is None:
        datestart = int(str(datetime.datetime.now()).split(' ')[0].replace('-','')) - 1
        datestart = str(datestart)
    if dateend is None:
        dateend = datetime.datetime.now().strftime( '%Y%m%d' )

    datestart = datetime.datetime.strptime( datestart, '%Y%m%d' )
    dateend = datetime.datetime.strptime( dateend, '%Y%m%d' )
    date_list = []
    date_list.append( datestart.strftime( '%Y%m%d' ) )
    while datestart < dateend:
        datestart += datetime.timedelta( days=+1 )
        date_list.append( datestart.strftime( '%Y%m%d' ) )
    return date_list
