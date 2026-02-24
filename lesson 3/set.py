from PIL.ImageChops import difference
from pandas.core.computation.expr import intersection
from streamlit import columns

my_set = {1, 2, 3, 4, 4, 5, 5, 5, 6, 7}
print(my_set)

set = set([1, 2, 3, 3, 4, 5, 6, 7])
print(set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_result_method = set1.union(set2)
union_result_operator = set1 | set2

print(union_result_operator)
print(union_result_method)

intersection_result_method = set1.intersection(set2)
intersection_result_operator = set1 & set2

print(intersection_result_operator)
print(intersection_result_method)

difference_result_method = set1.difference(set2)
difference_result_operator = set1 - set2

print(difference_result_method)
print(difference_result_operator)

symmetric_difference_method = set1.symmetric_difference(set2)
symmetric_difference_operator = set1 ^ set2

print(symmetric_difference_method)
print(symmetric_difference_operator)

my_set = {1,2,3}

my_set.add(7)

my_set.remove(3)

my_set.discard(8)

print(my_set)

my_set.clear()

print(my_set)

user1_interests = {"music", "movies", "travel"}
user2_interests = {"movies", "reading", "cooking"}

common_interests = user1_interests.intersection(user2_interests)
print(common_interests)

colors = {"blue", "red", "green"}
color = "green"
print(color in colors)
print(color not in colors)

