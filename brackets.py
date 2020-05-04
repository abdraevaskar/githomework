s = input('Enter some brackets: ')
def isBalanced(s):
    def brackets(s):
        all_br = ['()', '{}', '[]']
        while any(x in s for x in all_br):
            for i in all_br:
                s = s.replace(i, '')
        return not s
    if brackets(s):
        return 'YES'
    else: return 'NO'
print(isBalanced(s))

