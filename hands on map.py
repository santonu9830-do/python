list1 = [1, 2, 3]
list2 = [4, 5, 6]


result = map(lambda x, y: x + y, list1, list2)
print(list(result))

def sqr(x):
    return x * x

result = map(sqr, list1)
print(list(result))