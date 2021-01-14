import boto3
from boto3.session import Session
import datetime
dt_now = datetime.datetime.now()
year=dt_now.year
mon=dt_now.month
day=dt_now.day
if day!=1:
    day1=day-1
elif day==1:
    if mon==1:
        mon=12
        day1=31
    elif mon==2:
        mon=mon-1
        day1=28
    elif mon==3 or mon==5 or mon==7 or mon==8 or mon==10:
        mon=mon-1
        day1=31
    else:
        mon=mon-1
        day1=30
print(mon)
print(day1)
if mon==12 and day1==31:
    year=year-1
if mon<=9:
    fname = 'cowrie.json.'+str(year)+'-0'+str(mon)+'-'+str(day1)
    if day1<=9:
        fname = 'cowrie.json.'+str(year)+'-0'+str(mon)+'-0'+str(day1)
    else:
        fname = 'cowrie.json.'+str(year)+'-0'+str(mon)+'-'+str(day1)
elif mon>=9:
    if day1<=9:
        fname = 'cowrie.json.'+str(year)+'-'+str(mon)+'-0'+str(day1)
    else:
        fname = 'cowrie.json.'+str(year)+'-'+str(mon)+'-'+str(day1)
print(fname)
s3 = boto3.resource('s3')
bucket = s3.Bucket('AWS bucket name')
bucket.upload_file('path'+str(fname), 'path/'+str(fname))