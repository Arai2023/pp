#1 список квадратов 
n = int(input())
i=1
while(i*i<=n):
    print(i*i)
    i+=1

#2 минимальный делитель
n = int(input())
div = 2
while n%div!=0:
    div+=1
print(div)

#3 степень двойки
n = int(input())
i =1
while 2**i<=n:
    i+=1
print(i-1, 2**(i-1))

#4 утренняя пробежка
a = int(input())
b = int(input())
i=1
while a<=b:
    if a==b:
        break
    a+=a/10
    i+=1
print(i)

#5 длина последовательности
n=1
i=0
while n!=0:
    i+=1
    print(i-1)

#6 сумма последовательности
sum = 0
now = int(input())
while now!=0:
    sum+=now
    now = int(input())
print(sum)

#7 cреднее значение последовательности
n = int(input())
k=0
sum =0
while n!=0:
    sum+=n
    k+=1
    n = int(input())
print(sum/k)

#8 максимум последовательности
a = int(input())
max = a
while a!=0:
    if a>max:
        max = a
    a = int(input())
print(max)

#9 индекс максимума последовательности
max =0
index_max = -1
element = -1
len = 0
while element!=0:
    element = int(input())
    if element > max:
        max = element
        index_max = len
    len +=1
print(index_max)

#10 четные
n = int(input())
k=0
while n!=0:
    if n%2==0:
        k+=1
print(k)

#11 больше пред
a = int(input())
ans = 0
while a!=0:
    b = int(input())
    if b!=0 and a<b:
        ans+=1
    a=b
print(ans)

#12 vtoroi max
n = int(input())
max = 0
max2 = 0
while n!=0:
    n = int(input())
    if  n>max:
        max =n
    if n > max2 and max2<max:
        max2 = n
print(n)

#13 raven max
n = int(input())
max = 0
k = 0
while n!=0:
    n = int(input())
    if n > max:
        max = n
        k =1
    elif n==max:
        k+=1
print(k)

#14  fibonachchi
n = int(input())
if n ==0:
    print(0)
else:
    a = 0
    b =1
    for i in range (2, n+1):
        a=b
        b = a+b
print(b)

#15 nomer fibonachchi
a = int(input())
if a ==0:
    print(0)
else :
    pr = 0
    next = 1
    n =1
    while next<= a:
        if next==a:
            print(n)
            break
        pr = next
        next= pr+next
        n+=1
    else:
       print(-1)

#16 max podriad
pr = -1
curr = 0
max =0
n = int(input())
while n!=0:
    if pr ==n:
        curr+=1
    else:
        pr=n
        max = max(max, curr)
        curr = 1
    n = int(input())
    max = max(max, curr)
print(max)





 