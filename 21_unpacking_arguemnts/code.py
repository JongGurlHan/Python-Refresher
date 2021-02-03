def multiply(*args):    
    #print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total 
 
# print(multiply(1, 3, 5))


def apply (*args, operator):
    if operator == "*":
        print(args)
        print(*args)
        return multiply(*args) #the reason for that is because we did not pass in individual arguemts to the multipy function
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1,3,6,7, operator ="*"))