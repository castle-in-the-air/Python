#要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#要生成[1x1, 2x2, 3x3, ..., 10x10]：
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


'''写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，
十分有用，多写几次，很快就可以熟悉这种语法。'''


#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]


#还可以使用两层循环，可以生成全排列：
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
#三层和三层以上的循环就很少用到了。


#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k, v in d.items():
...     print(k, '=', v)
...
y = B
x = A
z = C


#因此，列表生成式也可以使用两个变量来生成list：
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']


#最后把一个list中所有的字符串变成小写：
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']

#if...else...
>>> [x if x % 2 == 0 else -x for x in range(1, 11)]
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

#注意！！！在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。#