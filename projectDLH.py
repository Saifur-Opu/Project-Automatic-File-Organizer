#!/usr/bin/env python3

# Read input (example format — adjust based on actual problem)
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Element-wise addition
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])

# Print result
print(result)