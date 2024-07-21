#pbar_v2
import time
def pbar_engine(length,comp):
    #main progress bar generating script
    if length<comp:
        exit()
    bar = "["
    for i in range(0,comp,1):
        bar = bar + "#"
    for i in range(0,length-comp,1):
        bar = bar + "-"
    return bar + "]"
def pbar_animate(length_ANI,wait_time):
    #animation script running on pbar_engine
    for i in range(0,length_ANI,1):
        print(pbar_engine(length_ANI,i+1))
        time.sleep(wait_time)
