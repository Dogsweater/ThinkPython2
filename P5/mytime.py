import time

def modify_time(time):
    time=int(time)
    day_now=time//(60*60*24)
    time=time-day_now*(60*60*24)
    hour_now=time//(60*60)
    time=time-hour_now*(60*60)
    minute_now=time//(60)
    second_now=time % 60
    print('现在距离纪元时间有',day_now,'天',minute_now,'小时',second_now,'秒')
    print('请珍惜这个伟大的纪元！')
    
now_=time.time()

modify_time(now_)