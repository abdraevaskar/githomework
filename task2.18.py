year = int(input('Enter the year: '))
def a(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        return('entered year')
    else: return('leap year')
print(a(year))
