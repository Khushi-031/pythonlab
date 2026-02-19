num = 4

while num <= 804:
    if (num // 4) % 2 == 1:
        print(num, end=", ")
    else:
        print(-num, end=", ")
    num = num + 4