import re
file = open("C:/Users/iztel/OneDrive/Рабочий стол/git/TSIS5/tasks/text.txt", 'r', encoding="UTF8")
result = re.findall("[a-z]+_[a-z]+", file.read())
print(result)
