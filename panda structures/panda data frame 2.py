import pandas

# creating data frame from series
dict1 = {'one': pandas.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': pandas.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pandas.DataFrame(dict1, index=['a', 'b', 'c', 'd'])
print(df)

# selecting indexes for data frame
df2 = pandas.DataFrame(dict1, index=['d', 'b', 'a'])
print(df2)

# choosing columns
df3 = pandas.DataFrame(dict1, index=['d', 'b', 'a'], columns=['two', 'one', 'three'])
print(df3)

# creating data frames from a list of array
df4 = pandas.DataFrame({'one': [1., 2., 3.], 'two': [3., 2., 4.]}, columns=['one', 'two'])
print(df4)
