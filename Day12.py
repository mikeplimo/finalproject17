x = 1
while x < 10000:
    if x % 3 == 0 and x % 11 == 0:
        print("motorcycle")
    elif x % 3 == 0:
        print("bicycle")
    elif x % 11 == 0:
        print("car")
    else:
        print(x)
    x = x + 1
