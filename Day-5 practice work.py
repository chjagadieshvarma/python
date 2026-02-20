# print 1 to 100 numbers using while loop
"""
num=0
while num<=100:
    print(num,end=" ")
    num+=1
"""

# print 1 to 100 numbers using for loop
"""
for i in range(1,101):
    print(i,end=",")
"""

#print even numbers between 10 to 40
"""
for i in range (10,41):
    if i%2==0:
        print(i,end=" ")
"""
"""
for i in range(10,41,2):
    print(i,end=",")
"""
"""
for num in range(10,41,1):
    if num>=10 and num<=41 and num%2==0:
        print(num,end=" ")
        num+=1
"""

#print odd numbers between 1 to 50
"""
for i in range(1,50,2):
    print(i)
"""
"""
for i in range(1,50):
    if i%2!=0:
        print(i,end=",")
"""
#find number is even or odd from list of numbers
"""
lst=[1,2,3,4,5,6,7,8,9]
for i in range(0,10,1):
    if lst[i]%2==0:
        print(lst[i],"is even number")
    elif lst[i]%2!=0:
        print(lst[i],"is odd number")
"""

#sum of even numbers upto n numbers

num=int(input())
sum=0
for i in range(2,num+1,2):
        sum+=i
print(sum)

#sum of odd numbers upto n numbers
"""
num=int(input())
sum=0
for i in range(1,num+1,2):
    sum+=i
print(sum)
"""















