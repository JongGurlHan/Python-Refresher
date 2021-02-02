# lambda fucntion is a different type of function which doesn't have a name
# and is only used to return values

# lambda fucntions are exclusively used to operate on inputs and return outputs.
# They are almost never used to perform actions.

# def add(x,y):
#     return x + y

add = lambda x,y: x+y

print(add(5,7))