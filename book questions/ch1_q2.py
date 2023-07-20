print("Enter the sides of the triangle")
myinput = input()
arr = myinput.split()
semi = 0
for i in range(0, len(arr)):
    arr[i] = int(arr[i])
    semi += arr[i]
semi /= 2
print('Semi perimeter =', semi)
area = (semi * (semi - arr[0]) * (semi - arr[1]) * (semi - arr[2])) ** 0.5
print('Area =', area)
