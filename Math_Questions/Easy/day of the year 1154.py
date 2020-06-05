date = "2019-01-09"
date = "2019-02-10"
date = "2003-03-01"
date = "2004-03-01"
sp = date.split('-')
year = int(sp[0])
month = int(sp[1])
day = int(sp[2])
days = 0
months  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if month == 1:
    days = day
elif month == 2:
    days = 31 + day
else:
    days = sum(months[:month-1])
    days += day
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                days+=1

        else:
            days+=1
print(days)