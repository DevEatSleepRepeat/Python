from datetime import datetime
today = datetime.now()
year = today.strftime('%Y')
days = today.strftime('%D')
hour = today.strftime('%H')
miut = today.strftime('%M')
sect = today.strftime('%S')
stamp = ("On "+days+" At "+hour+"."+miut+"."+sect)
print(stamp)
