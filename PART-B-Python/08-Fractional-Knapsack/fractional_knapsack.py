def knapsack(profit, weight, capacity):
    ratio = [(profit[i]/weight[i], i) for i in range(len(profit))]
    ratio.sort(reverse=True)

    total = 0

    for r, i in ratio:
        if weight[i] <= capacity:
            capacity -= weight[i]
            total += profit[i]
        else:
            total += r * capacity
            break

    return total

n = int(input("Enter number of items: "))
profit = []
weight = []

for i in range(n):
    p = int(input("Profit: "))
    w = int(input("Weight: "))
    profit.append(p)
    weight.append(w)

cap = int(input("Capacity: "))

print("Max Profit:", knapsack(profit, weight, cap))