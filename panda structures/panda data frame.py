import pandas

# data frames with lists
data = [['Aakash', 35], ['Aman', 17], ['Omkar', 25]]
Dataframe1 = pandas.DataFrame(data, columns=['Name', 'Age'], index=[10, 11, 12])
print(Dataframe1)

# slicing works on dataframes as well
print(Dataframe1[1:])

# data frames with dictionaries
data = {'Name': ['Ajay', 'Rahul', 'Rohit', 'Omkar'], 'Age': [35, 17, 25, 30]}
dataframe2 = pandas.DataFrame(data, index=[100, 101, 102, 103])
print(dataframe2)

# slicing of dataframes from dictionaries
print(dataframe2[:2])

# can also select a single column
print(dataframe2['Name'])
