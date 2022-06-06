Steps to solving this problem
  Step 1: Create copy of both nodes and calculate the length of each node
    - Logic: It is safe to assume that if the 2 nodes are of different length, any values before the index of the difference will not be the interesction point.
  Step 2: Based on which has the longer length, move the nodes length number of times to skip the redundant values to save on run time.
  Step 3: Compare the values of following node to find the proper intersection point, returning either of the 2 nodes as both points to the intersection point.

CURRENT TIME COMPLEXITY: O(m+n), m and n being the size of each node.


Challenge:
  Attempt to implement a hashmap to decrease running time.
