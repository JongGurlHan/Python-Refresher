def add(x,y):
    return x + y

# nums = [3,5]
# print(add(*nums)) # 3 for x, 5 for y

nums = {"x": 15, "y": 25}
print(add(nums["x"], nums["y"]))

print(add(**nums))
#** : okay, you've got a dictionay with two keys, what I'm gonna pass in each key as a named arguemt,
# and the value is going to be that associated with the key