list_ = input('Enter new list of numbers: ').split(' ')
step = int(input('Enter your step: '))
list_int = list(map(int, list_))
if step > 0:
    print(list_int[2:] + list_int[:2])
elif step < 0:
    print(list_int[-2:] + list_int[:-2])

