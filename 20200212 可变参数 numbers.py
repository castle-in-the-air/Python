def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
	
'''
>>> calc(1, 2)
5
>>> calc()
0
'''

'''
如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])
14
'''

'''
这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

>>> nums = [1, 2, 3]
>>> calc(*nums)
14
'''

#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

