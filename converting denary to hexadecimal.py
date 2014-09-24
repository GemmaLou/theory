#Gemma Buckle
#18/09/2014
#converting denary to binary to hexadecimal
denary_value = int(input("Please enter a denary integer: "))
binary_string = ""
while denary_value > 0:
    denary_string = CStr(denary_value)
    binary_string = Cstr(denary_value%2)
    denary_value = denary_value//2
endwhile
print("The binary equivalent is {0}".format(binary_string))
