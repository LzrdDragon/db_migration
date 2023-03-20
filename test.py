import datetime


some = datetime.datetime.strptime('2019-12-26 14:07:49.000', '%Y-%m-%d %H:%M:%S.%f')
print(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(31622400/86400))

print(datetime.datetime.now() + datetime.timedelta(31622400/86400) - datetime.datetime.now())
fut = datetime.datetime.now() + datetime.timedelta(31622400/86400)
difference = fut - datetime.datetime.now()

print(difference.days)
