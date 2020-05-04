a = input('input number A:')
b = input('input number B:')
c = [i for i in range(int(a), int(b) + 1) if int(a) < int(b)]
print(c)