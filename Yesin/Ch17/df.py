x = 121
# x = 10

def isPlindrome(x: int) -> bool:
    if x < 0:
        return False
    
    else:
        i = 0
        while i < x:
            x = x * 10 + x % 10
            x /= 10
        return x == i or x == i/10

print(isPlindrome(10))
