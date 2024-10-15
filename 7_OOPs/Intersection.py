class Line_Intersection:
    def __init__(self, a, b, c, d):
        self.x1 = a
        self.x2 = b
        self.y1 = c
        self.y2 = d

    def check_intersection(l1,l2):
        orientation = (l1.y2-l1.y1)*(l2.x1-l1.x2)-(l1.x2-l1.x1)*(l2.y1-l1.y2)



Line1 = Line_Intersection(2,3,1,5)
Line2 = Line_Intersection(2,3,1,5)

Line1.check_intersection(Line2)