import datetime


# [모듈].[객체].함수()
nowtime = datetime.datetime.now()
print('현재 날짜와 시간 : {}'.format(nowtime))

today = datetime.date(2024, 3, 21)
print('현재 날짜와 시간 : {}'.format(today))

lastDay = datetime.date(2024, 4, 30)
print('종강일 : {}'.format(lastDay))

t1 = datetime.time(21,30,0)
print('현재시간 : {}'.format(t1)) 

t2 = datetime.time(21,50,0)
print('수업종료 : {}'.format(t2))

today = datetime.datetime.now()
print( datetime.datetime.today().strftime('%Y-%m-%d') )


print('{} 년'.format( today.year) )
print('{} 월'.format( today.month ) )
print( '%02d' % today.month )   # leading zero
print('{} 일'.format( today.day) )
print('{} 시'.format( today.hour) )
print('{} 분'.format( today.minute) )
print('{} 초'.format( today.second) )




