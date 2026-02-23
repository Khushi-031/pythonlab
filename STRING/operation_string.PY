sentence ="hello world"
print(sentence.isalpha())
str2 ="hello"
print(str2.isalpha())
str3="hello 123"
print(str3.isalnum())
str4= "hello123"
print(str4.isalnum())
print("-----------TO FIND NUMBER OF ALPHABETS----------")
sentence =input("enter a sentence:")
count =0
for x in sentence:
    if(x.isalpha()):
        count=count+1
print("number of alphabets in sentence is :\n",count)
print("----------SPECIAL CHARACTERS IN SENTENCE--------")
sentence = input("enter a sentence   : ")
count=0
for ch in sentence :
    if not ch.isalnum():
        count+=1
print("special characters are : ",count)
print("---------upper function---------")
str5="A123"
print(str5.isupper()) 
print("#--------lower function----------")
print(str5.islower())
print("---------TITLE FUNCTION----------")
str6="Khushi Aggarwal"
print(str6.istitle())
print("#-------LOWER FUNCTION-(MODIFY THE STRING-------")
str7=str6.lower()
print("modified string is : ",str7)
print("#-------UPPER  FUNCTION-(MODIFY THE STRING-------")
str8=str6.upper()
print("modified string is : ",str8)
