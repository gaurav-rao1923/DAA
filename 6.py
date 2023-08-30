	
def knapsack_max_profit(weights, values, capacity):
 2 
 
    num_items = len(weights)
 3 
 
    # Create a table to store the maximum profit for each capacity and item
 4 
 
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]
 5 
 
    
 6 
 
    for i in range(1, num_items + 1):
 7 
 
        for j in range(1, capacity + 1):
 8 
 
            if weights[i - 1] <= j:
 9 
 
                # If the current item can be included, calculate the maximum of including and excluding it
 10 
 
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
 11 
 
            else:
 12 
 
                # If the current item cannot be included, take the value from the previous row
 13 
 
                dp[i][j] = dp[i - 1][j]
 14 
 
    
 15 
 
    return dp[num_items][capacity]
 16 
 
 17 
 
# Example usage
 18 
 
weights = [2, 3, 4, 5]  # Weights of the coffee beans in pounds
 19 
 
values = [10, 20, 30, 40]  # Values (cost in rupees) of the coffee beans
 20 
 
capacity = 10  # Capacity of the bag in pounds
 21 
 
max_profit = knapsack_max_profit(weights, values, capacity)
 22 
 
print("Maximum Profit:", max_profit)
