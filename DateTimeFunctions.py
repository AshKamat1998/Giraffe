from datetime import date
from datetime import  time
from datetime import  datetime
tdate = date.today()
tmonth= tdate.month
tyear= tdate.year

print(tdate)
print(tmonth)
print(tyear)
t = (datetime.now())
print(t)
print(t.strftime("%a") +" " + t.strftime("%A")+" " + t.strftime("%d")+" " + t.strftime("%D")+" " + t.strftime("%B"))