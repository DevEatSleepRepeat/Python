import time
wait = time.sleep
print('  - - - Raspberry Pi CM4 Builder! - - -')
print('-----------------------------------------')
wait(2.5)
base_mn = 'CM4'
user_mn = base_mn
#wireless = 0,1 n/y
print('Do you want wireless capability? (y/n)')
if input('') == "y":
    user_mn = user_mn + '1'
else:
    user_mn = user_mn + '0'
print('-----------------------------------------')
wait(1.5)
wait(0)
#ram = 01,02,04,08 in gb
print('How much ram do you want?\n1gb, 2gb, 4gb, or 8gb\n')
ram = '0'+input('Enter RAM Size (Ex. 1, 2, 4, or 8): ')
user_mn = user_mn + ram
print('-----------------------------------------')
wait(1.5)
#storage = 000,008,016,032 in gb
bef_storage = input('How much Storage do you want \n1 - No Storage (Lite)\n2 - 8gb\n3 - 16gb\n4 - 32gb\n\nEnter storage option 1 to 4: ')
if bef_storage == '1':
    user_mn = user_mn + "000"
elif bef_storage == '2':
    user_mn = user_mn + "008"
elif bef_storage == '3':
    user_mn = user_mn + "016"
elif bef_storage == '4':
    user_mn = user_mn + "032"
print('-----------------------------------------')
wait(1.5)
final_mn = ('CM4 m/n: '+user_mn)
print(final_mn)
