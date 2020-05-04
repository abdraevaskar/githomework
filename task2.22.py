numbers = input('Введите числа: ').split(',')
def a(numbers):
    c = [i for i in numbers if int(i) > 0]
    b = [i for i in numbers if int(i) < 0]
    print(c)
    print(b)
a(numbers)