from pandas import read_csv
from matplotlib import pyplot
import numpy

data = read_csv("dataset.csv", sep=",")
print(data.head(50))

names = ['term', 'tags']

# dimensions of data
print(data.shape)

# attributes data type
print(data.dtypes)

# class distribution
count_class = data.groupby('tags').size()
print(count_class)


