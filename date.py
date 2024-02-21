#ex1
import datetime
print(datetime.datetime.now()-datetime.timedelta(days=5))

#ex2
import datetime
print("Yesterday was: ", datetime.datetime.now()-datetime.timedelta(days=1))
print("Today is:", datetime.datetime.now())
print("Tomorrow will be: ", datetime.datetime.now()+datetime.timedelta(days=1))

#ex3
import datetime
now=datetime.datetime.now()
print(now.replace(microsecond=0))

#ex4
import datetime
today=datetime.datetime.now()
few_days=int(input())
some_days_ago=today.replace(day=few_days)
arasi=today.day - some_days_ago.day
print(arasi)
print(arasi*24*60*60)