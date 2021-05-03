def mult(a, b):
    return a*b


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Point at ({}, {})'.format(self.x, self.y)
    
    def __eq__(self, b):
        if self.x == b.x and self.y == b.y:
            return True
        return False
    
    def __add__(self, b):
        return Point(self.x+b.x, self.y+b.y)
    