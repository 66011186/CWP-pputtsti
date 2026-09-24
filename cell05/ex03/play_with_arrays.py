#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [x + 2 for x in original_array if x > 5]
unique_set = set(new_array)

print(original_array)
print(unique_set)