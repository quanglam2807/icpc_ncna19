# Gabriel Palacios

import math

n = int(input())
num_list = list(map(int, input().split()))
total_days = 365
total_probability = 1
for day_index in range(n):
    total_probability *= total_days / (365 ** num_list[day_index])
    total_days -= 1
print(math.log10(total_probability))