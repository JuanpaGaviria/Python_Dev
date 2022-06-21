import calendar
import time

def fun_timestamp():
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)
    return ts

