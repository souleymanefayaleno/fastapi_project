# For & While Loops

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday"]

my_table = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]

print("\n")
for x in my_list:
    print(f"Happy {x}!")

print("\n")
for liste in my_table:
    print(liste)

print("\n")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now large or equal to 5")
