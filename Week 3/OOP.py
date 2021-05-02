class Pet:
    def __init__(self, a):
        print('Object is created')
        self.a = a
        self.b = 'Ten'
    
    def __repr__(self):
        return self.b+' as ' + str(self.a)
    
    def __eq__(self, b):
        return self.a==b.a
    
    def __index__(self, i):
        return i
    
    def __del__(self):
        print('Object Destroyed of value:', self.a)

A = Pet(10)
B = Pet(10)
# print(A==B)
# del A
print(B[0])