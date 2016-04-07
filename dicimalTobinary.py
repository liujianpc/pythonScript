def dec2bin(decnum):
   if decnum > 1:
       dec2bin(decnum//2)
   print(decnum % 2,end = '')

decnum = int(input("Enter an integer: "))
dec2bin(decnum)
