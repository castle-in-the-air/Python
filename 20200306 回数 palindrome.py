# define
def is_palindrome(n):
    return n == int(str(n)[::-1])
 
# test
palindromes = filter(is_palindrome, range(0, 1000))
print(list(palindromes))