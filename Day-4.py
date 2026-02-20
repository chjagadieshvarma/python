"""
x=int(input())
for i in range (x,10):
    print(i)

"""
"""
x=int(input())
while x<11:
    x=x+1
    print(x)
"""

"""
num=int(input())
if num>0 and num%2==0:
    print("The number is positive even number")
elif num>0 and num%2!=0:
    print("the number is positive odd number")
elif num<0 and num%2==0:
    print("the number is negative even number")
elif num<0 and num%2!=0:
    print("the number is negative odd number")
elif num == 0:
    print("Zero is neither even or odd")
else:
    print("enter a valid number")

"""


"""
#check the greatest number

num1,num2,num3=map(int,input().split(","))
if num1>num2 and num1>num3:
    print(num1,"first number is greater")
elif num2>num1 and num2>num3:
    print(num2,"second number is greater")
elif num3>num1 and num3>num2:
    print(num3,"third number is greater")
else :
    print("invalid")

"""