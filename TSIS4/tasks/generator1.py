n = int(input())
def square(n):
    i=1
    while i*i<=n:
        yield i*i
        i += 1 
for i in square(n):
    print(i)