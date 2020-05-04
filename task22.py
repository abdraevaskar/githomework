text = input('Ввести имя файла: ')
def a():
    lines = 0
    words = 0
    letters = 0
    for line in open(f'{text}.txt', 'r'):
        lines += 1
        letters += len(line.strip('.,:-()!?;)"\'\n}'))
        words += len(line.split())
    return f'Lines = {lines}, words = {words}, letters = {letters}'
print(a())

