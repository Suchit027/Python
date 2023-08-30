import re

pattern = re.compile(r'(e)g')
match_object = pattern.match('egg is nutritional food')
print(match_object.group(0))
print(match_object.span())

pattern = re.compile(r'(ab)*')
match_object = pattern.match(r'ababababab')
print(match_object.group())

pattern = re.compile(r'(a(b)c)d')
match_object = pattern.match(r'abcd')
print(match_object.groups())
