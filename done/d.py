# Quang Lam

n = int(input())

k = (n - 1) % 4
if k == 0 or k == 2:
    print('Either')
elif k == 1:
    print('Odd')
elif k == 3:
    print('Even')