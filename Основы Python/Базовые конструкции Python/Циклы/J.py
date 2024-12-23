class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, way, step):
        if way == 'СЕВЕР':
            self.y += step
        elif way == 'ЮГ':
            self.y -= step
        elif way == 'ВОСТОК':
            self.x += step
        else:
            self.x -= step
    
    def get_coord(self):
        return (self.x, self.y)


point = Point(0, 0)
while True:
    way = input()
    if way == 'СТОП':
        break
    steps = int(input())
    point.move(way, steps)

for i in point.get_coord()[::-1]:
    print(i)