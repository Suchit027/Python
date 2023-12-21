import re

a = 'hiiii bye'
pattern = re.compile(r'i*')
grp = pattern.findall(a)
print(grp)
