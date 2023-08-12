Maindata = 'From rahul.kumar@hct.ac.ae Sunday Jan 4 '
atpost = Maindata.find('@')
print(atpost)
print(Maindata[:atpost])
data = Maindata[:atpost]

# note split
name = data.split(" ")
print(name)

# note replace and how upper is used
print(name[1].replace('.', ' ').upper())
