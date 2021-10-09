var1=int(input("enter first num: "))
var2=int(input("enter ur second  num:"))
var3=int(input("enter ur third num: "))
if var1>var2:
    if var1>var3:
        print(var1,"is bigest num")
    else:
        print(var3,"is bigest num")
elif var2>var3:
    print(var2,"is bigest num")
else:
    print(var3,"is bigest")

