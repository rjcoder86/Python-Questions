import math



#####FINDING PRIME NO

## Method 1
# Big O(n)

n=12
s=sum(1 for i in range(2,n) if n%i==0 )
print('not prime') if s else print('prime')


n=20
for i in range(3,n):
    s = sum(1 for j in range(2, i) if i % j == 0)
    print(i) if not s else None



### Method 2
# Big O(sqrt(n))
# if number is not prime its first divisor is less than its sqr root

n=20
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        print('Not prime')
        break



### Method 3
# All prime number

for i in range(1,20):
    print(6*i+1,6*i-1)

num = int(input())
if (num == 1):
    print("Not prime")
else:
    if (num % 2 == 0 and num > 2):
        print("Not prime")
    else:
        for i in range(3, int(num ** (1 / 2)) + 1, 2): #stepping to avoid even numbers
            if num % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")

n = int(input())
if n % 2 == 0 or n == 1:  # for checking 1,2 and even numbers
    print('Prime') if n == 2 or n != 1 else print('Not prime')
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            print('Not prime')
            break
    else:
        print('Prime')
