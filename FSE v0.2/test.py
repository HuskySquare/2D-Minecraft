import pickle
import pprint

with open("trees.pickle", "rb") as f:
    treesList = pickle.load(f)

for y in range(len(treesList)):
    print(treesList[y])

with open("trees.pickle", "wb") as f:
    pickle.dump(treesList, f)
