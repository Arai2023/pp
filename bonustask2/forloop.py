#1 ряд 1
a = int(input())
b = int(input())
for x in range(a,b+1):
    print(x)


#2 ряд 2
a = int(input())
b = int(input())
if a<=b:
    for i in range(a, b+1):
        print(i)
elif a>b:
    for i in range(a, b-1, -1):
        print(i)

    
#3 ряд 3
a = int(input())
b = int(input())
for i in range(a-(a+1)%2, b-b%2, -2):
    print(i, end= ' ')

#4 Cумма десяти чисел
sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)

#5 Сумма н чисел
n = int(input())
sum = 0
for i in range(n):
    sum+=int(input())
print(sum)

#6 сумма кубов
n = int(input())
sum = 0
for i in range(1, n+1):
    sum +=i**3
print(sum)

#7 факториал
res = 1
n = int(input())
for i in range(1, n+1):
    res*=i
print(res)

#8 сумма факториалов
res = 1
sum = 0
n = int(input())
for i in range(1, n+1):
    res*=i
    sum+=res
print(sum)

#9 количество нулей
k = 0
for i in range(int(input())):
    if(int(input())== 0):
        k+=1
print(k)

#10 лесенка
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, sep=' ', end=' ')

#11 потерянная карточка
n = int(input())
sum = 0
for i in range(1, n+1):
    sum+=i
for i in range(n-1):
    sum -=int(input())
print(sum)

