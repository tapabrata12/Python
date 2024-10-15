class Point:
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return f'<{self.x_cod},{self.y_cod}>'

    def euclidian_dist(self,other):

        part1 = (other.x_cod - self.x_cod)**2
        part2 = (other.y_cod - self.y_cod)**2
        distance = (part1 + part2)**.5
        return distance

    def dist_from_origin(self):
        return (self.x_cod**2 + self.y_cod**2)**.5



class Line:
    def __init__(self, A, B,C):
        self.A = A
        self.B = B
        self.C = C


    def __str__(self):
        return f'{self.A}x + {self.B}y + {self.C}'


    def point_lies(self):
        p1 = Point(int(input("Enter X coordinate: ")), int(input("Enter Y coordinate: ")))
        if self.A * p1.x_cod + self.B * p1.y_cod + self.C == 0:
            return 'Lies on the line'

        else:
            return 'Do not lie on this line'

    def distance_point_line(line):
        p1 = Point(int(input("Enter X coordinate: ")), int(input("Enter Y coordinate: ")))
        return abs(line.A*p1.x_cod + line.B*p1.y_cod + line.C) / (line.A**2 + line.B**2)**.5





# L = Line(int(input("Enter A: ")), int(input("Enter B: ")),int(input("Enter C: ")))

# print(L.distance_point_line())

# L.point_lies()

# p1 = Point(int(input("Enter X coordinate: ")), int(input("Enter Y coordinate: ")))

# p2 = Point(int(input("Enter X coordinate: ")), int(input("Enter Y coordinate: ")))

# p1.euclidian_dist(p2)
# p1.dist_from_origin()