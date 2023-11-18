items = [
[2, 40], # Item 1: weight = 2, value = 40 
 [5, 30], # Item 2: weight = 5, value = 30

[10, 50], # Item 3: weight = 10, value = 50

[5, 10], # Item 4: weight = 5, value = 10

[7, 70], # Item 5: weight = 7, value = 70

[3, 15], # Item 6: weight = 3, value = 15

[2, 60], # Item 7: weight = 2, value = 60

[4, 80], # Item 8: weight = 4, value = 80

[9, 20], # Item 9: weight = 9, value = 20

[6, 50] # Item 10: weight = 6, value = 50
]
knapsack_capacity = 15 # Maximum knapsack capacity
 

def knapsack_greedy(items,capacity):
    sorted_list=sorted(items, key=lambda items:items[1],reverse=True)
    max_capacity=0
    backpack=[]
    end=0
    for i in sorted_list:
        if i[0]<=capacity:
            backpack.append(i)
            max_capacity=i[0]+max_capacity
            capacity=capacity-i[0]
            end=end + i[1]
    print(backpack,"\ncapacity:",max_capacity,"\nbackpack has value of:",end)
    
def knapsack_0_1(items,capacity):
    sorted_list=sorted(items, key=lambda items:items[1],reverse=True)
    max_capacity=0
    backpack=[]
    for i in sorted_list:
        if i[0]<=capacity:
            backpack.append(i)
            max_capacity=i[0]+max_capacity
            capacity=capacity-i[0]
            break
    return backpack, max_capacity
def knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            weight, value = items[i - 1]
            if weight > j: 
                dp[i][j] = dp[i - 1][j] 
            else:
                dp[i][j] = max(dp[i - 1][j], value + dp[i - 1][j - weight]) 
    return dp[n][capacity]



knapsack_greedy(items,knapsack_capacity)
print(knapsack_0_1(items,knapsack_capacity))
print(knapsack(items,10))