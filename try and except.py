x = 'Hi'
errormsg = ''
try:
    y = int(x)
#  if error will go to except
except:
    y = -1
    errormsg = '\nIncorrect msg'

print('First Try:', y, errormsg)
