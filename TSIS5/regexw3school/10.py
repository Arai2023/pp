import re
txt = "hello planet"
x = re.findall("he.{2}o", txt)
print(x)
