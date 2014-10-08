#Gemma Buckle
#08/10/2014
#password creator

password_length=int(input("How many characters do you want your password to be?"))
while password_length!=0:
    password_choices=(97,122 or 65,90 or 48,57)
    import random
    password_text=(chr(random.randint(password_choices)))
    password=password_text
    password_length=password_length-1
    print(password)
