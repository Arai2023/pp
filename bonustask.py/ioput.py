#1 sum
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#2 triangle
b = int(input())
h = int(input())
s = 1/2 * b *h
print(s)

#3 apples
k = int(input())
n = int(input())
l = n // k 
m = n % k
print(l)
print(m)

#4  watch
n = int(input())
s = n // 60
l = n % 60
if s==24:
    print(0, l)
else:
    print(s, l)


#5 hello, harry!
n = str(input())
print("Hello," , n ,"!")

#6 next and previous
n = int(input())
l = n-1
s = n+1
print("The next number for the number", n, "is", s)
print("The previous number for the number", n, "is",l)

#7 desks
a = int(input())
b= int(input())
c=int(input())
k = (a+1)//2 + (b+1)//2 + (c+1)//2
print(k)

#8 
a = int(input())
b = int(input())
l = int(input())
N = int(input())
print(str((2*a*N - a)+2*l+2*b*(N-1)))
