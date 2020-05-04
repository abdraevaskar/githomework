s = input(str('Enter new string:'))
if 'f' in s:
    print(s.index('f'))
    print(s.rindex('f'))
elif s.count('f') == 1:
    print(s.index('f'))
else: print('')