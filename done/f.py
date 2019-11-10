# Quang Lam

m = int(input())
lst = []

for i in range(m):
    lst.append(int(input()))

lst.sort()

# After sorting, I attempted to remove all duplicated elements from the list to improve speed
# Doing this would still return correct answers for the provided test cases
# but gave "Wrong Answer" for other cases when submitting to Kattis
# I didn't manage to figure it out before running out of time :(
# lst = [lst[i] for i in range(len(lst)) if i == 0 or lst[i - 1] != lst[i]]

total_sum = 0
for i in range(len(lst)):
    total_sum += lst[i]
half_sum = total_sum / 2

def solve():
    i = 0
    j = len(lst) - 1
    l = lst[i]
    r = lst[j]

    while True:
        if j - 1 > 0 and r + lst[j - 1] <= half_sum:
            j -= 1
            r += lst[j]
        elif i + 1 < len(lst) and l + lst[i + 1] <= half_sum:
            i += 1
            l += lst[i]
        elif i + 1 < j:
            return lst[i + 1]
        elif lst[i] + 1 < lst[j]:
            return lst[i] + 1
        else:
            return lst[i]

        if i + 1 < len(lst) and l + lst[i + 1] <= half_sum and l < r:
            i += 1
            l += lst[i]

        if j - 1 > 0 and r + lst[j - 1] <= half_sum and r < l:
            j -= 1
            r += lst[j]

print(solve())