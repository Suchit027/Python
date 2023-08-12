import pandas

d = {
    # 'Name': pandas.Series(['Rahul', 'Omkar', 'Samarth']),
    'Age': pandas.Series([22, 23, 45]),
    'Height': pandas.Series([170.2, 170.4, 180])
}

Dataframe = pandas.DataFrame(d)
print(Dataframe.std())
print(Dataframe.describe())
print(Dataframe.median())
print(Dataframe.mean())
print(Dataframe['Height'].mode())
