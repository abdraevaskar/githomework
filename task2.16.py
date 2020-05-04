List_Of_Int = input('Enter the list of integers: ')
b = List_Of_Int.split(',')
def list_(b):
    c = []
    for i in b:
        if int(i) < 0:
            c.append('-1')
        elif int(i) > 0:
            c.append('1')
        else: c.append('0')
    return c
print(list_(b))