class time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self,other):
      total_second=self.second+other.second
      extraminute=total_second//60
      seconds=total_second%60
      total_minute=self.minute+other.minute+extraminute
      extrahour=total_minute//60
      minutes=total_minute%60
      hours=self.hour+other.hour+extrahour
      return time(hours,minutes,seconds)
    def display(self):
      print(f"{self.hour:}:{self.minute:}:{self.second:}")
h1=int(input("enter the hours:"))
m1=int(input("enter the minutes:"))
s1=int(input("enter the second:"))
t1=time(h1,m1,s1)
h2=int(input("enter the hours:"))
m2=int(input("enter the minutes:"))
s2=int(input("enter the second:"))
t2=time(h2,m2,s2)
t3=t1+t2
t3.display()


