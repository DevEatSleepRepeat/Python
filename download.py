import os
import time

wait = time.sleep

def get_size():
    print("\nEnter the size of the file (In Megabytes)\n")
    slc_siz = int(input("[main@python3]:"))*8
    return slc_siz
def get_speed():
    print('''Select Your Speed
    5G---100 mbps
    LTE--30 mbps
    4G---14 mbps
    3G---3 mbps
    ''')
    slc_spd = input("[main@python3]:")
    if slc_spd == "5g" or slc_spd == "5G":
        speed = 100
    elif slc_spd == "lte" or slc_spd == "LTE":
        speed = 30
    elif slc_spd == "4g" or slc_spd == "4G":
        speed = 14
    elif slc_spd == "3g" or slc_spd == "3G":
        speed = 3
    else:
        print("Invalid Selection - TRY AGAIN")


    return speed

def DT_now(speed, size):
    calculation = (size / speed)
    return calculation

def pbar_creator(mx, mn, progress):
    bar_prog = mn
    oppos = mx - progress
    base = ("[")
    temp_text = ""
    for i in range(mn, (progress), 1):
        temp_text += "#"
    bar = base + temp_text
    temp_text = ""
    for i in range(0, oppos, 1):
        temp_text += "-"
    bar = bar + temp_text + "]"
    return bar

def PbDR(speed, size):
    os.system("clear")
    time = DT_now(speed, size)
    w_time = (time / 22)
    for i in range(0, 22, 1):
        print(pbar_creator(21, 0, i)+"  "+str(round(time-(w_time*i), 2))+" Remaining")
        wait(w_time)
        os.system("clear")
    print("Your "+str(size/8)+" megabyte download has compleated is "+str(time)+" seconds.")

PbDR(get_speed(), get_size())
