import os, time
from datetime import datetime
now = datetime.now()
hr = int(now.strftime("%H"))
noon = "AM"
mi = now.strftime("%M")
if hr > 12:
    noon = "PM"
    hr -= 12
    hr = ("-"+str(hr))
finaltime = (str(hr)+":"+str(mi))

print("""
    |---|
    |---|
    |---|
    /---\\
""" + "   |" + finaltime + """|
   |"""+ ("-"+noon+"--") +"""|
    \---/
    |---|
    |---|
    |---|
""")
