user = input('Enter your text: ')
import re
pattern = r"\W"
a = len(re.findall(pattern,user))
print(len(user) - a)
