test_dict = {'codingal': 2, 'is': 1, 'best': 1}
print("The original dictionary is:" + str(test_dict))

k = 2
res = 0
for key in test_dict.values():
    if key == k:
        res += 1
print("The frequency of " + str(k) + " is: " + str(res))