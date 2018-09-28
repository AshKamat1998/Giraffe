class Vector:
    'Defines a Vector'
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)
    def __str__(self):
        return 'Vector (%d, %d)' %(self.a, self.b)

V1 = Vector(2,3)
V2 = Vector(5,8)
print(V1+V2)