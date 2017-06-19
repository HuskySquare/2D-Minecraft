from pygame import *
tree = image.load("tree_trunk_60.png")

for y in range(20):
    tree.set_at((0, y), tree.get_at((2, y)))
    tree.set_at((1, y), tree.get_at((2, y)))

image.save(tree, "tree_trunktest.png")
