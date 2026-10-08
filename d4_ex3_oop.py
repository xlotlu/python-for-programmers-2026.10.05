# același lucru
class MyCls:
    pass
class MyCls():
    pass
class MyCls(object):
    pass

class MyCls:
    def __init__(self): # dă semnătura clasei
        # `self` este echivalentul lui `this`
        # din alte limbaje
        print("»", self)
        # doar că este pasat explicit

# același lucru:
class MyCls:
    def __init__(x):
        print("»", x)

class MyCls:
    # init face procedura de _inițializare_
    # a obiectului. nu este constructor-ul!
    def __init__(self, x):
        # inițializare = whatever
        print(x)
        self.my_attribute = x

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_from_origin(self):
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )


#from functools import cached_property

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        print("» mă execut")
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )

class Vector:
   def __init__(self, distance, angle):
       self.distance = distance
       self.angle = angle

   def __repr__(self):
       return f"Vector({self.distance}, {self.angle})"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        distance = math.sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2
        )
        angle = 42 # chosen by true trigonometry
        return Vector(distance, angle)

    def __truediv__(self, value):
        return Point(self.x / 2, self.y / 2)

#### inheritance ###
class ThreeDPoint(Point):
    pass

# îl modificăm pe Point să fie mult mai generic
# (scăpăm de hardcodări cu "Point")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_tuple(self):
        return self.x, self.y

    def __repr__(self):
        return f"{self.__class__.__name__}{repr(self.as_tuple())}"

    def __str__(self):
        return str(self.as_tuple())

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        distance = math.sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2
        )
        angle = 42 # chosen by true trigonometry
        return Vector(distance, angle)

    def __truediv__(self, value):
        return Point(self.x / 2, self.y / 2)

class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def as_tuple(self):
        return self.x, self.y, self.z

    def __eq__(self, other):
        # magia lui super():
        # returnează o referință a obiectului curent
        # în contextul clasei părinte
        return super().__eq__(other) and self.z == other.z
        # ^^ echivalent cu:
        #    (self.x == other.x and self.y == other.y) and self.z == other.z

# continuăm abstractizarea cu as_tuple()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_tuple(self):
        return self.x, self.y

    def __repr__(self):
        return f"{self.__class__.__name__}{repr(self.as_tuple())}"

    def __str__(self):
        return str(self.as_tuple())

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )
    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def __add__(self, other):
        return self.__class__(
            *map(sum,
                 zip(self.as_tuple(),
                     other.as_tuple(),
                     strict=True)
            )
        )

    def __sub__(self, other):
        distance = math.sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2
        )
        angle = 42 # chosen by true trigonometry
        return Vector(distance, angle)

    def __truediv__(self, value):
        return self.__class__(
            *map(
                lambda coord: coord / value,
                self.as_tuple()
            )
        )

class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def as_tuple(self):
        return self.x, self.y, self.z

    def translate(self, dx, dy, dz):
        super().translate(dx, dy)
        self.z += dz
