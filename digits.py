#py1_sumofdigits

num =int(input())
sum=0
while(num!=0):
    n=num%10                #o/p_15=6
    sum=sum+n
    num=num//10
print(sum)

#PY2_reverse

num =int(input())
reverse=0
while(num>0):             #o/p_1505=5051
    n=num%10                
    reverse=(reverse*10)+n
    num=num//10
print(reverse)
                    [OR]
    num=input():
    n=num[::-1]
    print(n)
    
#py3 palindrome or not

num=input()
n=num[::-1]
if(n==num):                                       #o/p:amma,amma is a palindrome;dhinesh,dhinesh is not palindrome
    print(num," is a palindrome")
else:
    print(num," is not palindrome")
    
    #PY4 Amstrong number or not
    
num=int(input())
sum=0
temp=num
while(temp>0):
    d=temp%10                       #O/P=135,135 is Amstrong number;134 is not Amstrong number
    sum+=d**3
    temp=temp//10
if(num==sum):
    print(num," is a Amstrong number")
else:
    print(num," is not Amstrong number")
 #amstrong between two interval
num1=int(input())
num2=int(input())
for i in range(num1,num2+1):
    order = len(str(i))
    sum=0
    temp=i
    while(temp>0):
        d=temp%10
        sum+=d**order
        temp=temp//10
    if (i==sum):
        print (i)

    #BINARY TO DECIMAL
    
    t=int(input())
for _ in range(t):
    n=input()
    print(int(n,2))
    
    
    
    
