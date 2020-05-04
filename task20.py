# 1) google_kazakstan.txt
# 2) google_paris.txt
# 3)google_uar.txt
# 4)google_kyrgystan.txt
# 5)google_san_francisco.txt
# 6)google_germany.txt
# 7)google_moscow.txt
# 8)google_sweden.txt
user = input('Введите Hello чтобы выбрать страну офиса: ')
countries = ('1)Kazakstan', '2)Paris', '3)UAR', '4)Kyrgystan', '5)San - Francisco', 
'6)Germany', '7)Moscow', '8)Sweden')
for i in countries:
    print(i)
office = input('Введите номер страны: ')
for i in office:
    if office == '1':
        with open('google_kazakstan.txt', 'w') as f:
            f.write(input('Напишите жалобу:'))
    elif office == '2':
        with open('google_paris.txt', 'w') as f:
            f.write(input('Напишите жалобу:'))
    elif office == '3':
        with open('google_uar.txt', 'w') as f:
            f.write(input('Напишите жалобу:'))
    elif office == '4':
        with open('google_kyrgystan.txt', 'w') as f:
            f.write(input('Напишите жалобу:'))      
    elif office == '5':
        with open('google_san_francisco.txt', 'w') as f:
            f.write(input('Напишите жалобу:')) 
    elif office == '6':
        with open('google_germany.txt', 'w') as f:
            f.write(input('Напишите жалобу:'))
    elif office == '7':
        with open('google_moscow.txt', 'w') as f:
            f.write(input('Напишите жалобу:'))
    elif office == '8':
        with open('google_sweden.txt', 'w') as f:
            f.write(input('Напишите жалобу:'))
    else: break              

