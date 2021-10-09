# a={'a':["saloni"],'b':["subreena"]}
# for i in a:
#     a[i] = a[i][0]
# print(a)


# test_list = [{"id" : 1, "data" : "HappY"},
#              {"id" : 2, "data" : "BirthDaY"},
#              {"id" : 3, "data" : "Rash"}]
# for i in range(len(test_list)):
#     if test_list[i]['id'] == 2:
#         del test_list[i]
#         break
# print (test_list)


# dic={'a':2,'b':9,'c':5}
# sum=0
# for i in dic.values():
#     sum=sum+i
# print(sum)


# b={'a':20,'b':50,'c':70}
# c={}
# for i in b:
#     f=float(b[i])
#     c.update({i:f})
# print(c)


# dic={1:{1:'one',2:'two'},2:{3:'three',4:'four'},3:{5:'five',6:'six'}}
# sum=0
# for i in dic:
#     for j in dic[i]:
#         sum=sum+j
# print(sum)


# a=[1,2,3,4,5]
# b={}
# for i in a[::-1]:
#     b={i:b}
# print(b)

# a={0:10,1:20}
# a[2]=30
# print(a)

# a=int(input("Enter your number: "))
# b={}
# i=1
# while i<=a:
#     key=input("Enter your key: ")
#     value=int(input("Enter your value: "))
#     b[key]=value
#     i+=1
# print(b)

# num=int(input("enter ur number: "))    # second number is 3.
# b=num//100
# c=b%10
# if c==3:
#     print("yes")
# else:
#     print("no")


# user=input("enter ur number: ")                  #second last number is 3.
# if "3" in (user) and user[2]=="3":
#     print("yes")
# else:
    # print("no")   

# x="global"
# def my_fun():
#     # x=x*2
#     print(x)
# my_fun()
# print(x)


# i=1
# while i<=5:
#     print(end="")
#     j=0
#     while j<=i:
#         print ( j*"*",end="")
#         j+=1
#         print()
#     i+=1

# if  True:
#     if False:
#         if True:
#             print("A")
# if True:
#     if True:
#         if True:
#             print("b")
# if True:
#     if False:
#         print("c")
# elif True:
#     if True:
#         print("D")

# a, b = 10, 20   # ternary operator example.
# if a != b:
#     if a > b:
#         print("a is greater than b")    #  condition ? value_if_true : value_if_false
#     else:
#         print("b is greater than a")
# else:
#     print("Both a and b are equal")

# a={1:23,2:4,5:7}
# print(sorted(a.values()))

# for i,j in sorted(a.items()):
#     print(i,a[i],j)


# sorted_a=dict(sorted(a.items()))
# print(sorted_a)

# dt = {5:4, 1:6, 6:3}

# sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}

# print(sorted_dt)

# a=["nikita"]
# i=0
# c={}
# while i<len(a): 
#     j=0
#     e={}
#     while j<len(a[i]):
#         b=a[i][j]
#         a[i]=b
        # e.update({j:b})
#         j+=1
#     i+=1
# print(e)

# def my_max(a):
#     i=0
#     max=a[i]
#     for i in a:
#         if i>max:
#             max=i
#         return max
# d=my_max([82,9,52,8,7,6,50])
# print(d)

