# #1 it will print 5 
# def a():
#     return 5
# print(a())

# #2 it will be an error , but it returned 10! 
# def a():
#     return 5
# print(a()+a())

# #3 most likely just 5
# def a():
#     return 5
#     return 10
# print(a())

# #4 it will return only 5 
# def a():
#     return 5
#     print(10)
# print(a())

# #5 it will print 5 , but it printed none since there is no return!
# def a():
#     print(5)
# x = a()
# print(x)

# #6 since there is no return, the output is nothing, ERROR
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# #7 you cant add up strings as math equations! 
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# #8 it returns 100 , then returns 10 
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# #9 it returns 7 , 14 ,21 
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# #10 returns 8
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# #11 it prints 500 , 300 ,500 at the end 500 ,and i am wrong
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# #12 prints 500,500,300,500
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

#13 500 ,500 ,300, 300 
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# #14 1,3,2
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

# #15 1,3,5,10
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)











