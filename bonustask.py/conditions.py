#1 
a = int(input())
b = int(input())
if a >b :
    print(b)
else :
    print(a)

#2 
x = int(input())
if x > 0:
    print(1)
elif x<0:
    print(-1)
else :
    print(0)

#3 
a = int(input())
b= int(input())
c = int(input())
d = int(input())
if (a+b+c+d)%2==0:
    print("YES")
else:
    print("NO")

#4 
a = int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print("YES")
else:
    print("NO")

#5
a= int(input())
b = int(input())
c = int(input())
if a<=b and a<=c:
    print(a)
elif b<=a and b<=c:
    print(b)
else:
    print(c)
    
#6
a= int(input())
b = int(input())
c = int(input())
if a==b==c:
    print(3)
elif a==b or a==c or b==c:
    print(2)
else:
    print(0)

#7
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==c or b==d:
    print("YES")
else:
    print("NO")

#8
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a + 1) < c or (c+1) < a or (b+1) < d or (d+1) < b :
    print("NO")
else:
    print("YES")

#9
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a+b==c+d or a+d==b+c :
    print("YES")
else:
    print("NO")

#10
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==c or b==d or a+b==c+d or a+d==b+c :
    print("YES")
else:
    print("NO")

#11
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (abs(a-c)==1 and abs(b-d)==2) or (abs(b-d)==2 and abs(a-c)==1):
    print("YES")
else:
    print("NO")

#12
n = int(input())
m = int(input())
k = int(input())
if k<n*m and ((k%n == 0) or (k%m==0)):
    print("YES")
else:
    print("NO")

#13
n= int(input())
m =int(input())
x = int(input())
y = int(input())
if n>m:
    n,m = m,n
if x >= n/2:
    x= n-x
if y>= m/2:
    y = m-y
if x <y:
    print(x)
else:
    print(y)

