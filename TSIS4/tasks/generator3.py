n = int(input())
def check(n):
    a = 0
    while a<=n:
        if a%3==0 and a%4==0:
            yield a
        a+=1 
for i in check(n):
    print(i)