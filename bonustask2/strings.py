#1 делаем срезы
s =input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

#2 количество слов
print(input().count(' ') + 1)

#3 две половинки
s = input()
print(s[len(s)+1])

#4 переставить два слова 
s = input()
a = s[:s.find(' ')]
b = s[s.find(' ')+1:]
print(b + ' ' + a)

#5 первое и последнее вхождения
s = input()
if s.count('f') ==1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))

#6 второе вхождение
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else :
    print(s.find('f', s.find('f')+1))

#7 удаление фрагмента
s = input()
print(s[:s.find('h')] + s[s.rfind('h') + 1:])

#8 обращение фрагмента
s = input()
a = s[:s.find('h')]
b = s[s.find('h'):s.rfind['h']+1]
c = s[s.rfind('h')+1]
s = a+b[::-1] + c
print(s)

#9 замена подстроки
print(input().replace('1', 'one'))

#10 удаление символа
print(input().replace('@', ''))

#11 замена внутри фрагмента
s = input()
s = s.replace('h', 'H', s.count('h')-1)
s = s.replace('H', 'h', 1)
print(s)

#12 удалить каждый третий символ
s = input()
t = ''
for i in range(len(s)):
    if i%3!=0:
        t = t+s[i]
print(t)

