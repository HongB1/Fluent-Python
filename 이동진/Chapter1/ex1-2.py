from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print("v1 + v2: ", v1 + v2)
    
    print("")
    v = Vector(3, 4)
    print("v1: ", v1)
    print("The norm of v: ", abs(v))
    print("v * 3: ", v * 3)  # 3 * v는 안 된다.
    print("The norm of v * 3: ", abs(3 * v))
