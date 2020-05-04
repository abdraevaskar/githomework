N = int(input('Enter the number: '))
print({i**2 for i in range(1, N+1) if i**2 < N})
