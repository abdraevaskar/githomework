numbers = input('Введите список чисел: ').split(',')
def a(numbers):
    x = [numbers.count(i) for i in numbers if int(i) % 2 == 0]
    b = [numbers.count(i) for i in numbers if int(i) % 2 != 0]
    print(f'{len(x)} четных чисел, {len(b)} нечетных чисел')
a(numbers)