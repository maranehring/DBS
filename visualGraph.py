## Initialisation
import main2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
newList=[]
with open("aa.txt","r") as b:
    b=b.readlines()
    for i in b:
        newList.append(i.strip())
#print(len(newList))
secondList=[]
counter=0
for i in range(len(newList)):
    secondList.append(0)

df = pd.DataFrame({
    'x': newList,'y': secondList
})

np.random.seed(4)
k = 3
# centroids[i] = [x, y]
centroids = {
    i + 1: [np.random.randint(0, 4), np.random.randint(0,4)]
    for i in range(k)
}

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.show()
