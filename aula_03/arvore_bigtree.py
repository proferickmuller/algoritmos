# https://builtin.com/articles/tree-python

import bigtree

root = bigtree.Node(1)
a = bigtree.Node(2, parent=root)
b = bigtree.Node(9, parent=root)

root.show()

c = bigtree.Node(3, parent=a)
d = bigtree.Node(4, parent=a)
e = bigtree.Node(5, parent=a)

f = bigtree.Node(6, parent=b)
g = bigtree.Node(7, parent=b)

root.show()
