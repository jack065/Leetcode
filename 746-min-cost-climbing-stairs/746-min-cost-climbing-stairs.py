class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # HOW DOES THE CODE WORK???!!!!
        # Add a zero at the end of cost to denote the end of the array. 
        cost.append(0)
        
        # Decrement the array till we reach the last index.
        # Since in python, len(cost) - 1 gives us the zero value, we want set our starting index to a value such that should it increment by 2,
        # it would reach zero, hence we use len(cost) - 3. We should then decrement it by one to reach the smallest index.
        for i in range(len(cost) - 3, -1, -1):
            # Adding the costs up. Overwrite the value at index i by adding the min number if you take one step compared to two steps.
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
         
        # Catch case, should the array be only 2 indices long. Also the lowest value will always be at index one or two so it works for other cases too!
        return min(cost[i], cost[i+1])