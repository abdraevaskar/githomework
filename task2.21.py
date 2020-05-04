string = input('Введите предложение: ').split(' ')
def a(string):
    return max(string, key = lambda i: len(i))
print(a(string))