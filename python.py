print('hello world') #Day_1
#A=input('What is your name?')
#print('Nice to meet you,'+ A)


#Day2
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
Area= [hall,kit,liv ,bed ,bath]

# Print areas
print(Area)
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
fam=[ 'liz',1.73 , 'emma', 1.68, 'mom', 1.71, 'dad', 1.89 ]
fam1= fam + ['smk', 3]
print(fam)
fam[1]=2
print(fam[1])
fam[0:3]=['Lisa', 3, 'enna']
print(fam)
print(fam[3:5])
print(fam[:5])
del fam1[8:10]
print(fam1)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas)
# Print out second element from areas
print(areas[0])

# Print out last element from areas
print(areas[9])

# Print out the area of the living room
print(areas[5])
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print("Downstairs:", downstairs)
print("Upstairs:", upstairs)


#Day3
import numpy as np
baseball = [180, 245, 210, 188, 176, 209, 200]
np_baseball= np.array(baseball)
print(type(np_baseball))
np_2= np.array([[1.73, 1.68,1.71,1.89, 1.79],[65.4, 59.2, 63.6, 88.4,68.7]])
print(np_2)
print(np_2.shape)
print(np_2[1, : ])
np_2D= np.array(np_2[0, : ])
print(np_2D)
print(np.mean(np_2D))
print(np.median(np_2D))
print(np.average(np_2D))
x = [[1, 2, 3, 4, 5], ["DataCamp", "Python", "Practice", "Exercises"], [True, False, 0, 1]]

# Indexing to get the second list and then slicing to get the first three elements
print(x[0][:3])
