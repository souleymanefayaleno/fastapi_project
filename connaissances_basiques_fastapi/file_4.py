# map, filter, compréhension de liste
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# map
result1 = map(lambda x: x*x, liste)

# filter
result2 = filter(lambda x: x % x, liste)

# compréhension de liste
result3 = [x*x for x in liste]

result4 = [x for x in liste if x % 2 == 0]

print(f"la liste result1 est : {result1} \n")
print(f"la liste result3 est : {result3} \n")
print(f"la liste result2 est : {result2} \n")
print(f"la liste result4 est : {result4} \n")
