for item in range(2, 102, 2):
    if item ** 2 > 1000:
        print('breaking item', item)
        break
    print(item ** 2)