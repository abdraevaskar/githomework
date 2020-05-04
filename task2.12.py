def convert_temp(scale = None, temp = None):
    if scale == "F":
        return (temp - 32.0) * (5.0/9.0)
    elif scale == "C":
        return (temp * (9.0/5.0)) + 32.0 
    else:
        print("Error!!!")
temp = int(input("Temperature: " ))
scale = input("Select F or C: " )
m = convert_temp(scale, temp)
print(f'{temp} degrees {scale} is {m} degrees')







