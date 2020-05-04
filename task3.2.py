s = input('enter: ')
def funnyString(s): 
    r = s[::-1]
    s_ascii = list(s.encode('latin-1'))
    r_ascii = list(r.encode('latin-1'))
    for i in range(1, len(s_ascii)):
        if abs(s_ascii[i] - s_ascii[i-1]) != abs(r_ascii[i] - r_ascii[i-1]):
            return 'Not Funny'
    return 'Funny'
print(funnyString(s))
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the funnyString function below.
# def funnyString(s): 
#     r = s[::-1]
#     s_ascii = list(s.encode('latin-1'))
#     r_ascii = list(r.encode('latin-1'))
#     for i in range(1, len(s_ascii)):
#         if abs(s_ascii[i] - s_ascii[i-1]) != abs(r_ascii[i] - r_ascii[i-1]):
#             return 'Not Funny'
#     return 'Funny'
    


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input())

#     for q_itr in range(q):
#         s = input()

#         result = funnyString(s)

#         fptr.write(result + '\n')

#     fptr.close()