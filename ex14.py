import pandas as pd

sd = pd.Series([1, 2, None, 4], index = ['a', 'b', 'c', 'd'])

print(sd, end = "\n\n")
print(sd.shape, end = "\n\n")
print(sd.size, end = "\n\n")
print(sd.isna(), end = "\n\n")

print(f"sd[0] : {sd['a']}")
print(f"sd[1] : {sd[1]}")
print(f"sd[2] : {sd['c'] + 1}")   # still nan (not a number)