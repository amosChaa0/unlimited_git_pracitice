# def check(num):
#     if num==1:
#         print(num ," is not prime number")
#     elif num>1:
#         for i in range (2, num):
#             if num%i==0:
#                 return"the number is not prime"
#             else:
#                 return "the number is prime"
# num=int(input("enter a number"))
# a=check(num)
# print(a)
def check_prime(a):
    for i in range(2,int(a/2)+1):
        if a%i==0:
            return False
    return True
num=int(input("enter a number"))
if check_prime(num):
    print("prime")
else:
    print("not prime")
