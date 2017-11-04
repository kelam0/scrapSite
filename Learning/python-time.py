# -*- coding: utf-8 -*-
"""
Keeping Time
Created on Sun Aug 14 16:36:14 2016

@author: Malek
"""

##time uses
#import time
#
#startTime = time.time() #seconds between unix epoch and now i.e. 01/01/1970 00:00:00 and now
#for i in range(1,10000):
#    i = i * i
#endTime = time.time()
#
#print('Result = %s and only took %s seconds!' % (str(i), str(round(endTime-startTime,4))))
#
##pause the script for 5 seconds:
#time.sleep(5)


##datetime module
#import datetime
#tnow = datetime.datetime.now()
#
#print(tnow)
#print(tnow.year, tnow.month, tnow.day)
#print(tnow.hour, tnow.minute, tnow.second)
#
#anotherday = datetime.datetime(2015,1,1,0,0,0,0)
#print(anotherday)
#
#daysBetweenDates = datetime.timedelta(weeks=1, days=4, hours=6, minutes=9, seconds=30)
#print(daysBetweenDates.total_seconds())
##no years, months, hours or minutes available
#print(daysBetweenDates.days, daysBetweenDates.seconds, daysBetweenDates.microseconds)
#
#print(str(daysBetweenDates))
#print(str(daysBetweenDates + datetime.timedelta(days=1000)))
#
##strftime allows you to format a datetime
#oct21st = datetime.datetime(2016, 10, 21, 16, 29, 0)
#print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
#print(oct21st.strftime('%I:%M %p'))
#print(oct21st.strftime("%B of '%y"))
#
##strptime allows you to load a string as a datetime
#datetime.datetime.strptime('October 21, 2016', '%B %d, %Y')
#datetime.datetime.strptime('2016/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
#datetime.datetime.strptime("October of '16", "%B of '%y")
#datetime.datetime.strptime("November of '63", "%B of '%y")


##wait until a time and date and can be useful when multithreading.
#import datetime
#import time
#
#specialday = datetime.datetime(2016,9,1,0,0,0)
#while datetime.datetime.now() < specialday:
#    time.sleep(1)
#    
#print("It's special day bruh!")


