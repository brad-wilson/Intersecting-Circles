import math


def det(a, b, c, d):
    # Matrix determinant
    return a * d - b * c


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'Vector(%d, %d, %d)' % (self.x, self.y, self.z)

    def __repr__(self):
        return 'Vector(%d, %d, %d)' % (self.x, self.y, self.z)

    def __add__(self, other):
        # Vector addition
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        # Vector subtraction
        return Vector(self.x - other.x, self.y - other.y, self.z + other.z)

    def mag(self):
        # Vector magnitude/modulus
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def cross(self, other):
        # Cross product of 2 vectors
        return Vector(det(self.y, self.z, other.y, other.z), - det(self.x, self.z, other.x, other.z), det(self.x, self.y, other.x, other.y))

    def dot(self, other):
        # Dot product of 2 vectors
        return self.x*other.x + self.y*other.y + self.z*other.z

    def intersection(self, other, r1, r2):
        # Returns 2 points of intersection (x,y) of the two circles related to the receivers and their distance from the transmitter signal
        d = Vector.mag(self - other)
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = math.sqrt(r1**2 - a**2)
        P = Vector(((a / d) * (self.x - other.x) + other.x), ((a / d) * (self.y - other.y) + other.y), 0)
        int1x = P.x + (h / d) * (self.y - other.y)
        int1y = P.y - (h / d) * (self.x - other.x)
        int2x = P.x - (h / d) * (self.y - other.y)
        int2y = P.y + (h / d) * (self.x - other.x)
        return [Vector(int1x, int1y, 0), Vector(int2x, int2y, 0)]

    def distances(self, others):
        # Given a point, this returns the two closest points to that point
        return sorted(others, key=lambda x: Vector.mag(self - x))[:2]

    def centroid2d(self, other1, other2):
        # Returns the centroid vector of the triangle formed by 3 points
        return Vector(self.x/3 + other1.x/3 + other2.x/3, self.y/3 + other1.y/3 + other2.y/3, self.z/3 + other1.z/3 + other2.z/3)


p1x = float(input("input X-coordinate of Receiver1 here:"))
p1y = float(input("input Y-coordinate of Receiver1 here:"))

p1 = Vector(int(p1x), int(p1y), 0)
print("Receiver1 at",p1)

p2x = float(input("input X-coordinate of Receiver2 here:"))
p2y = float(input("input Y-coordinate of Receiver2 here:"))

p2 = Vector(int(p2x), int(p2y), 0)
print("Receiver2 at",p2)

p3x = float(input("input X-coordinate of Receiver3 here:"))
p3y = float(input("input Y-coordinate of Receiver3 here:"))

p3 = Vector(int(p3x), int(p3y), 0)
print("Receiver3 at",p3)

signal1 = float(input("input measured distance separating Receiver1 and the transmitter here:"))
signal2 = float(input("input measured distance separating Receiver2 and the transmitter here:"))
signal3 = float(input("input measured distance separating Receiver3 and the transmitter here:"))

a = list(Vector.intersection(p1, p2, signal1, signal2))
b = list(Vector.intersection(p2, p3, signal1, signal2))
c = list(Vector.intersection(p1, p3, signal1, signal2))
points = a + b + c
print(points)

# Finds the list of points forming the center triangle
s_list = []
for point in points:
    pointsCopy = list(points)
    pointsCopy.remove(point)
    s = Vector.mag(point - pointsCopy[0]) + Vector.mag(point - pointsCopy[1])
    print("magnitude sum is",s)
    s_list.append((point, s))

triangle = sorted(s_list, key=lambda x: x[1])[:3]
print(Vector.centroid2d(triangle[0][0], triangle[1][0], triangle[2][0]))
