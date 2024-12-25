from datetime import datetime, timedelta

# a=datetime.now()
# print(datetime.utcnow())
# print(datetime.utcnow() - timedelta(days=10, hours=10))

# b=datetime.strftime(a)

a = '05-20-2020 13:01'
a = datetime.strptime(a, '%m-%d-%Y %H:%M')
print(a)

print(a.strftime('%m-%Y-%Y %M:%H'))
# dtobj = datetime.fromisoformat(a)
#
# print(dtobj)
# print(type(dtobj))
# # print(repr(dtobj))
