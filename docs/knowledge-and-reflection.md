# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

>  They are all hash functions because they all share the property of taking in a key and returning a value.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> 1. Is straightforward, efficient, and returns the same value every time; however, it will always produce a collision and there is no security or scalability.
> 2. Is efficient and has middling levels of collisions depending on the size. Security wise it can work, but it is not bulletproof by any means.
> 3. Not as efficient but much more secure. Chances of collisions are inconsistent. The same input will almost certainly not return the same output.
> 4. Simpler then 2, not as simple as 1. Collisions are probable. Security is on the low end. Determinism is high.
> 5. High security, low efficiency. The same input will almost certainly not return the same output.

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> 1. Security: The whole reason to implement a hash map is to obfuscate information making it secure. 
> 2. Determinism: Secondly you want to make sure that you are able to get the results you need when you are searching and inputting. 
> 3. Efficiency: Lastly, while it needs to be secure, it still needs to operate and perform it's function in a timely manner.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> Pearson hash provides a good balance between security, efficiency, and collision prevention (I would have liked to do the pearson but couldn't get it right and did inbuilt)

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> "Import random, creating a consistent randomized number from 42. Create a table to and shuffle it to provide randomness and security, this also increases it's sensitivity. Lastly create the key by looping through each character to provide a given consistent key based on the random values. "

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> 1. Create a hash map with a randomized number.
> 2. Each hash map should be a playerlist.
> 3. Create a player, hashing a key.
> 4. Insert the player into the hash map based on it's key location.

## Reflection

1. What was the most challenging aspect of this task?

> Wrapping my head around the concept of the hash table/map.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> I would key it to a spot. If it was blocked then I would iterate until I found an available slot. Drawback with this version is the bigger and more filled the hash map gets the worse the performance will be, this also doesn't take into account if players would be removed.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.