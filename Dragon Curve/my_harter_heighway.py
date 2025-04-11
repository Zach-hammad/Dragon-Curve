from math import sqrt
from engr131_plot_module import make_2D_plot

class Vertex:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def next_gen(self, other, direction=1):
        xm = (self.x + other.x) / 2
        ym = (self.y + other.y) / 2
        b = (other.y - self.y) / 2
        c = (other.x - self.x) / 2
        if direction == 1:
            return Vertex(xm - b, ym + c)
        else:
            return Vertex(xm + b, ym - c)

    def generate_dragon(self, point1, point2, N):
        list_points = [point1, point2]
        direction = 1
        for _ in range(N):
            new_points = [list_points[0]]
            for i in range(len(list_points) - 1):
                new_point = list_points[i].next_gen(list_points[i + 1], direction)
                new_points.append(new_point)
                new_points.append(list_points[i + 1])
                direction *= -1  # Alternate direction
            list_points = new_points
        return list_points

if __name__ == '__main__':
    point1 = input("Enter point 1 (x, y format):\n")
    point2 = input("Enter point 2 (x, y format):\n")
    point1x, point1y = map(float, point1.split(','))
    point2x, point2y = map(float, point2.split(','))
    point1 = Vertex(point1x, point1y)
    point2 = Vertex(point2x, point2y)
    gen = int(input("Enter Num gen:\n"))
    gen= range(gen)
    for i in gen:
        imgname = "Image {}".format(i+1)
        points = point1.generate_dragon(point1, point2, i)
        make_2D_plot(points, imgname)
        print('The generation-{} Dragon Curve has {} vertices.'.format(i, len(points)))
        print('Plot appears in {}.'.format(imgname))
