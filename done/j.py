# Kari Hoff & Gabriel Palacios

n = int(input())
rows = [""] * n
cols = [""] * n

correct = True

# Set up row and col lists
for rowIdx in range(n):
    row = input()
    rows[rowIdx] = row
    for colIdx in range(n):
        letter = row[colIdx]
        cols[colIdx] += letter

""" Initial Attempt """
# def LetterCounter(lst):
#     for index in range(len(lst)):
#         w_counter = 0
#         b_counter = 0
#         if lst[index] == "W":
#             w_counter += 1
#         else:
#             b_counter += 1
#     return w_counter == b_counter

# def checkCons(dimension):
#     cons = 0
#     prev = ""
#     for index in range(len(dimension)):
#         if dimension[index] == prev:
#             cons += 1
#         else:
#             cons = 1
#             prev = letter
#         if cons > 2:
#             return False
#     return True


for index in range(n):
    row = rows[index]
    col = cols[index]
    # Check that there are:
    # 1. not 3 consecutive in each row and col
    # 2. the count of W and B is the same
    if "WWW" in row:
        # print(f"There are 3 whites in this row: {row}")
        correct = False
    if "BBB" in row:
        # print(f"There are 3 blacks in this row: {row}")
        correct = False
    if "WWW" in col:
        # print(f"There are 3 whites in this col: {col}")
        correct = False
    if "BBB" in col:
        # print(f"There are 3 blacks in this col: {col}")
        correct = False
    if row.count("W") != row.count("B"):
        # print(f"There are an uneven number of whites and blacks in this row: {row}")
        correct = False
    if col.count("W") != col.count("B"):
        # print(f"There are an uneven number of whites and blacks in this col: {col}")
        correct = False

# Print Result (T:1 F:0)
if correct:
    print(1)
else:
    print(0)