print("ALGBoss\nSolving [Constant]+[Coefficient][Variable]=[Constant]\n")
term1 = int(input("Constant: "))
print("+")
coeff = int(input("Coefficient: "))
varib = input("Variable: ")
print("=")
term2 = int(input("Constant: "))
if term1 < 0:
    rs = term2+term1
    print(rs)
elif term1 > 0:
    rs = term2-term1
    print(rs)
else:
    print("ERROR")
final_rs = rs/coeff
print(varib,"=",final_rs)
