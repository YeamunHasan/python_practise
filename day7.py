# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict={'country':names, 'drives_right':dr, 'cars_per_cap': cpc}
# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)

print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']


# Specify row labels of cars
cars.index=row_labels
print(cars.loc[['US', 'IN']])

# Print cars again
print(cars)

df = pd.read_csv("D:\\New Python\\student.csv", index_col=0)
print(df)

row=df.iloc[[1,2,3], [1,2]]
print(row)