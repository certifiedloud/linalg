""" A python class to represent vectors """

class Vector(object):
    def __init__(self, coordinates):
        self.coordinates = tuple(coordinates)
        self.dimension = len(coordinates)

    def __str__(self):
        return "{}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        if self.dimension != v.dimension:
            raise ValueError("Vector dimensions must be the same")
        newCoords = []
        for i in range(self.dimension):
            newCoords.append(self.coordinates[i] + v.coordinates[i])
        return Vector(newCoords)

    def subtract(self, v):
        if self.dimension != v.dimension:
            raise ValueError("Vector dimensions must be the same")
        newCoords = []
        for i in range(self.dimension):
            newCoords.append(self.coordinates[i] - v.coordinates[i])
        return Vector(newCoords)

    def scalarMultiply(self, scalar):
        newCoords = []
        for i in range(self.dimension):
            newCoords.append(self.coordinates[i] * scalar)
        return Vector(newCoords)



if __name__ == "__main__":
    myVec1 = Vector([1,2,3])
    myVec2 = Vector([4,5,6])
    print("Vec1 {}".format(myVec1))
    print("Vec2 {}".format(myVec2))
    print("Vec1 + Vec2  = {}".format(myVec1.add(myVec2)))
    print("Vec1 - Vec2  = {}".format(myVec1.subtract(myVec2)))
    print("Vec1 * 2  = {}".format(myVec1.scalarMultiply(2)))
