def column_sum(lst):
    return list(map(sum, zip(*lst)))

lst = [[1, 5, 3], [2, 7, 8], [4, 6, 9]]
print(sum(column_sum(lst)))


