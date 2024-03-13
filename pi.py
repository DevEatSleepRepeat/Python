notsolved = True
a = 1
b = 1
def check(num,den):
    x = round(num/den,3)
    if x == 3.141:
        notsolved = False
        print("SOLVED"+str(num)+"/"+str(den))
        exit()
    return x

while notsolved:
    for i in range(1,100000):
        for j in range(1,100000):
            a+=1
            print(a,b,check(a,b))
        a=1
        b+=1


