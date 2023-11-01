#!/usr/bin/python3

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
union_set = set1.union(set2)
intersect_set = set1.intersection(set2)
diff_set = set2.difference(set1)
symetric_set = set1.symmetric_difference(set2)
is_subset = set1.issubset(set2)
is_superset_set = set1.issuperset(set2)
set_copy = set1.copy()
list_set = list(set1)
tuple_set = tuple(set1)
# clear_set = set_copy.clear()
# print(union_set)
# print(intersect_set)
# print(diff_set)
# print(symetric_set)
# print(is_superset_set)
# print(is_subset)
# print(set_copy)
# print(clear_set)
print(list_set)
print(tuple_set)