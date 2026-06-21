student_id = [1190, 1191, 1192]
student_name = ['Alice', 'Bob', 'Charlie']
details = zip(student_id, student_name)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for x, y in zip(list1, list2):
    print(x, y)

stocks = ['AAPL', 'GOOGLE', 'MSFT']
prices = [150, 2800, 300]

new_dict = dict(zip(stocks, prices))
print('\n{}'.format(new_dict))