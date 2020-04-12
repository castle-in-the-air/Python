numbers=[11,0,6,3,5,4,-1,2,-1,4,5,8,1,9,8,11,0,6,4,3,3,-1]
"""print(list(set(numbers)))
"""

uni=[]
for number in numbers:
    if number not in uni:
        uni.append(number)
uni.sort()
print(uni)