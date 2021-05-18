class Time:
    """  """
    
time=Time()
time.hour=3
time.minute=59
time.second=30


def print_time(time):
    print('(%.2d:%.2d:%.2d)'%(time.hour,time.minute,time.second))

#print_time(time)

def add_time(t1,t2):
    """
    if not valid_time(t1) and valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    """
    assert valid_time(t1) and valid_time(t2)
    seconds =time_to_int(t1)+time_to_int(t2)
    return int_to_time(seconds)
    
def time_to_int(time):
    minutes=time.hour*60 + time.minute
    seconds=minutes*60 +time.second
    return seconds

def int_to_time(seconds):
    time=Time()
    minutes,time.second = divmod(seconds,60)
    time.hour,time.minute = divmod(minutes,60)
    return time
    
def valid_time(time):
    if time.hour<0 or time.minute<0 or time.second <0:
        return False
    if time.minute>=60 or time.second >=60:
        return False
    return True
    
time2=Time()
time2.hour=2
time2.minute=10
time2.second=5

time3=add_time(time,time2)
print_time(time3)
