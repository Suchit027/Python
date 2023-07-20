print('Enter working hours and rate per hour')
myinput = input()
arr = myinput.split()
hour = int(arr[0])
rate = int(arr[1])
if hour > 30:
    pay = 30 * rate + (hour - 30) * 1.5 * rate
else:
    pay = hour * rate
print('Pay =', pay)
