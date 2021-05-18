def int_to_time(seconds):
    time=Time()
    minutes,time.second = divmod(seconds,60)
    time.hour,time.minute = divmod(minutes,60)
    return time

class Time: 
    #__init__的形参和类的属性名常常是相同的
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    #方法的第一个形参通常叫做self
    #__str__方法是一个特殊方法，它用来返回对象的字符串表达形式
    #当你打印对象时，Python会调用__str__方法
    def __str__(self):
        return('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))
    def time_to_int(time):
        minutes=time.hour*60+time.minute
        seconds=minutes*60+time.second
        return seconds
    def increment(self,seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    def is_after(self,other):
        return self.time_to_int()>other.time_to_int()
    #操作符重载
    #基于类型的分发
    def __add__(self,other):
        #isinstance()接受一个值和一个类对象，当此值是这个类对象时返回真
        if isinstance(other,Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    #当Time的对象出现在+的右边时：
    def __radd__(self,other):
        return self.__add__(other):
    def add_time(self,other):
        seconds=self.time_to_int()+other.time_to_int()
        return int_to_time(seconds)
        
        
  
time2=Time()
time2.hour=2
time2.minute=10
time2.second=5

#Time.print_time(time2)
#主体会被赋值给第一个形参
#time2.print_time()
#print(time2.time_to_int())
end = time2.increment(1377)
print(end)
print(time2.is_after(end))
start=Time(9,45)
duration=Time(1,35)
print(start+duration)