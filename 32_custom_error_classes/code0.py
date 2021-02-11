class test:
    def __repr__(self):
        return "__repr__ called!"
    def __str__(self):
        return "__str__ called!"

test_a = test()
print(test_a)

print(str(test_a))