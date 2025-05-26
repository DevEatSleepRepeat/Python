def multiply(a,b):
    out_m = 0
    for i in range(0,b):
        out_m+=a
    return out_m
#def devide(a,b):
    out_d = 0
    leftover = b
    while leftover>a:
        leftover -= a
        out += 1
    return out_d

print(multiply(2,3))