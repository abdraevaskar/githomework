""" Write a program that reads an integer number and prints its previous and
next numbers. See the examples below for the exact format your answers
should take. There shouldn't be a space before the period.
Remember that you can convert the numbers to strings using the function str.
(На английском языке что бы Вы научились пониматьThe next number for the number 179 is 180. The previous number for the
number 179 is 178.)
"""
number_ = input('number:')
print(f'The next number for the number {int(number_)} is {int(number_) + 1}. The previous number for the number {int(number_)} is {int(number_) - 1}')
