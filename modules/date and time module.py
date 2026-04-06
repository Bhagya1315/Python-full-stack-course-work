from datetime import date,time,datetime,timedelta
today = date.today()
print(today)

print(date(2026,3,31))



print("Year:",today.year)
print("Month:",today.month)
print("Day:",today.day)
print(today.weekday())
print(today.isoweekday())


now=time(16,38,18)
print(now)
print(now.hour)
print(now.minute)
print(now.second)


now=datetime.now()
print(now)



now=datetime.now()
print(now.strftime('%d%m%y %H%M%S'))
print(now.strftime('%d%m%y %I%M%S'))


print(now.strftime('%d%b%y %I%M%S'))


print(now.strftime('%d%B%y %H%M%S %p'))

print(now.strftime('%A %d %B %y %H%M%S %p'))


today = date.today()
now = datetime.now()


today_7 = today-timedelta(days=7)
print(today_7)

now_30 = now+timedelta(minutes=30)
print(now_30)




