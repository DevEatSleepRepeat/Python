from datetime import datetime
def dd(datetime1, datetime2):
    delta = datetime2 - datetime1
    return delta.days
today = datetime.now()
year = int(today.strftime('%Y'))
hour = int(today.strftime('%H'))
miut = int(today.strftime('%M'))
sect = int(today.strftime('%S'))
christmas = datetime(year, 12, 25)
day_till_christmas = dd(today, christmas)
seconds_till_christmas = (((day_till_christmas*24-hour)*60-miut)*60-sect)
print(f'You Have {seconds_till_christmas} seconds till Christmas!')
