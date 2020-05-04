string_ = input('Введите строку: ')
def a(string_):
    if string_[0::] == string_[::-1]:
        print('True')
    else: print('False')
a(string_)