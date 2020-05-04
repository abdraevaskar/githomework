
while True:
    print('Если хотите закрыть калькулятор, нажмите Enter')
    number_1 = input('Введите число 1:')
    a = input('Методы(*, /, +, -):')
    number_2 = input('Введите число 2:')
    if number_1 == '': 
        break
    else:
        if number_1.isdigit() and number_2.isdigit():
            if a == '+':
                print(float(number_1) + float(number_2))
            elif a == '-':
                print(float(number_1) - float(number_2))
            elif a == '*':
                print(float(number_1) * float(number_2))
            elif a == '/':
               if number_2 != 0:
                  print(float(number_1) / float(number_2))
               else:
                  try:
                     float(number1) / 0
                  except ZeroDivisionError:   
                     print('Деление на ноль!')
            else: print('Ошибка операции!')
        else: print('Неверные данные')