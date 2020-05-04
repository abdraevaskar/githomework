n = int(input())
def stepPerms(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2 
    else:
        return stepPerms(n-3) + stepPerms(n-2) + stepPerms(n-1)
print(stepPerms(n))
