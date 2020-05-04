a = int(input('enter your age:'))
if a % 2 == 0:
    print([i for i in range(0, a + 1) if i % 2 == 0])
else:
    print([i for i in range(0, a + 1) if i % 2 != 0])