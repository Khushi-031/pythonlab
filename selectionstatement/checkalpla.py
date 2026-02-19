ch = input("Enter a character: ")

if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
    print("It is an Alphabet")
else:
    if ch >= '0' and ch <= '9':
        print("It is a Digit")
    else:
        print("It is a Special Character")