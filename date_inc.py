from datetime import date, timedelta

y, m, d = [int(x) for x in input().split()]       # Ввод
day = int(input())
dt = date(y, m, d)

dt_td = dt + timedelta(days=day)                  # складываем дату и дни

print(dt_td.year, dt_td.month, dt_td.day)