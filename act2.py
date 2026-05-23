def cube(num):
    return num**3
def check(num):
    if num%3==0:
        print('The cube is:',cube(num))
    else:
        print('the number is not divisible by 3')
check(99)
