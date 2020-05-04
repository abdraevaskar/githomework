list_ = input('Enter new list: ')
list_ = list_.split(',')
item_ = input('Enter your item: ')
def a(list_, item_):
    return list_.count(f'{item_}')
print(list_)
print(a(list_, item_))