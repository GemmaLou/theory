#Gemma Buckle
#08/10/2014
#convert ascii to text, text to ascii

user_input=input("To convert ASCII code to text, input 'ascii'. To convert text to ASCII code, input 'text': ")
if user_input=="ascii":
    user_code=int(input("Please enter your ASCII code: "))
    output=chr(user_code)
    print("{0} as text is {1}.".format(user_code,output))
elif user_input=="text":
    user_text=input("Please enter your text value: ")
    output=ord(user_text)
    print("{0} as ASCII is {1}.".format(user_text,output))
