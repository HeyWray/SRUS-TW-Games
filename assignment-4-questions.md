# Step 1 – Knowledge Question (20-50 words)

```
"In your own words, describe what a Binary Search Tree (BST) is.
In addition, describe two important properties of a BST: depth and height. How are they different?"
```

A Binary Tree is a graph where each node consists of 0, 1, or 2 child nodes. A Binary Search Tree is the ability to search from the root of the tree outwards across each child to find or set new node values. 

Depth refers to how far into the tree the Node is. Height is the largest distance bewteen a node and it's furthest node child.

# Step 2 – Knowledge Question (50-80 words)

```
"In your own words, describe how an algorithm to find an item in a Binary Search Tree works."
```

An algorythm takes a given value and determines if it is higher or lower than a given node's value. If it is lower it will compare the node's lower/less than/left (if it exists) same with higher/greater then/right value.

# Step 3 – Knowledge Question (20-60 words)

```
"In your own words, describe what a balanced BST is."
```

A balanced BST is one that has a roughly even number of right and left nodes on either side. The root is generally the central value of the overall values of the tree.

# Step 8 - Knowledge Question
```
"With the newly balanced BST, how many steps does it take at most to find an existing item in the search tree?"
```

With a length of:
1- 1 steps,
2- 2 steps,
5- 3 steps,
10- 4 steps,
20- 5 steps,

While starting inefficient, the size of the BST has increase larger each time.

O(logn), according to https://dev.to/msnmongare/big-o-notation-cheatsheet-12m3