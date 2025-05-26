import time
weeks = 0
money = 1
while weeks < 100:
    money = int(money) * 2
    weeks += 1
    time.sleep(0.04)
    print(money)
