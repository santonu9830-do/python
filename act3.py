num = int(input("Please enter a number : "))
t = num
numLen = 0
while t > 0:
    numLen += 1
    t = int(t / 10)
if numLen >=4:
 numLen = int(numLen / 2)
 chk = 0
 while num > 0:
    rem = num % 10
    if chk==numLen:
       midone = rem
    elif chk==(numLen-1):
       midtwo = rem
    num = int(num / 10)
    chk += 1
    prod = midone * midtwo
 print("/nProduct of Mid digits (" + str(midone) + " and " + str(midtwo) + ") is : ", prod)
else:
    print("/nIt's not a four-digit number or more than 4 digits number!.")