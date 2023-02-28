n=int(input())
def odd(n):
    while n>=0:
        yield n
        n-=1
for i in odd(n):
 print(i)