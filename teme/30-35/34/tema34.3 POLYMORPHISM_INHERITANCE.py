# Task 3
# Create a base class Shape to draw flat shapes.
# Define the following methods:
# •	Show() — print info about a shape;
# •	Save() — save a shape to a file;
# •	Load() — read a shape from a file.
# Define the derived classes:
# •	Square — a square defined by the coordinates of the upper left corner
# and the side length;
# •	Rectangle — a rectangle with the specified coordinates of the upper
# left corner and dimensions;
# •	Circle — a circle with the specified coordinates of the center and radius;
# •	Ellipse — an ellipse with the specified coordinates of the top corner of a
# circumscribed rectangle with its sides parallel to the coordinate axes, and
# the dimensions of this rectangle.
# Create a list of shapes, save the shapes to a file, load into another list,
# and display information about each shape.


from abc import ABC, abstractmethod

# =======================
# Base class: Shape
# =======================


class Shape(ABC):
    @abstractmethod
    def show(self):
        """Print info about the shape."""
        pass

    @abstractmethod
    def save(self, file):
        """Save shape to file (one line)."""
        pass

    @staticmethod
    def load(file):
        """
        Read ONE line from file and return the corresponding Shape object.
        Return None if EOF (no more lines).
        """
        line = file.readline()
        if not line:
            return None  # EOF

        parts = line.strip().split()
        if not parts:
            return None

        shape_type = parts[0]

        if shape_type == "Square":
            # Square x y side
            x, y, side = map(float, parts[1:])
            return Square(x, y, side)

        elif shape_type == "Rectangle":
            # Rectangle x y width height
            x, y, width, height = map(float, parts[1:])
            return Rectangle(x, y, width, height)

        elif shape_type == "Circle":
            # Circle cx cy radius
            cx, cy, r = map(float, parts[1:])
            return Circle(cx, cy, r)

        elif shape_type == "Ellipse":
            # Ellipse x y width height
            x, y, width, height = map(float, parts[1:])
            return Ellipse(x, y, width, height)

        else:
            raise ValueError(f"Unknown shape type: {shape_type}")


# =======================
# Derived: Square
# =======================


class Square(Shape):
    def __init__(self, x, y, side):
        # (x, y) = coordonatele colțului stânga-sus
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        print(f"Square: top-left=({self.x}, {self.y}), side={self.side}")

    def save(self, file):
        # Format: Square x y side
        file.write(f"Square {self.x} {self.y} {self.side}\n")


# =======================
# Derived: Rectangle
# =======================


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        # (x, y) = coordonatele colțului stânga-sus
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(
            f"Rectangle: top-left=({self.x}, {self.y}), "
            f"width={self.width}, height={self.height}"
        )

    def save(self, file):
        # Format: Rectangle x y width height
        file.write(f"Rectangle {self.x} {self.y} {self.width} {self.height}\n")


# =======================
# Derived: Circle
# =======================


class Circle(Shape):
    def __init__(self, cx, cy, radius):
        # (cx, cy) = coordonatele centrului
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def show(self):
        print(f"Circle: center=({self.cx}, {self.cy}), radius={self.radius}")

    def save(self, file):
        # Format: Circle cx cy radius
        file.write(f"Circle {self.cx} {self.cy} {self.radius}\n")


# =======================
# Derived: Ellipse
# =======================


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        """
        (x, y) = coordonatele colțului stânga-sus ale
        dreptunghiului circumscris, cu laturile paralele cu axele.
        width, height = dimensiunile acelui dreptunghi
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(
            f"Ellipse: bounding-rect top-left=({self.x}, {self.y}), "
            f"width={self.width}, height={self.height}"
        )

    def save(self, file):
        # Format: Ellipse x y width height
        file.write(f"Ellipse {self.x} {self.y} {self.width} {self.height}\n")


# =======================
# Demo: create, save, load, show
# =======================

if __name__ == "__main__":
    # 1) Creăm o listă de forme
    shapes = [
        Square(0, 0, 10),
        Rectangle(5, 5, 20, 10),
        Circle(15, 15, 7),
        Ellipse(2, 2, 12, 8),
    ]

    # 2) Salvăm în fișier
    filename = "shapes.txt"
    with open(filename, "w") as f:
        for s in shapes:
            s.save(f)

    # 3) Încărcăm din fișier într-o altă listă
    loaded_shapes = []
    with open(filename, "r") as f:
        while True:
            shape = Shape.load(f)
            if shape is None:
                break
            loaded_shapes.append(shape)

    # 4) Afișăm informații despre fiecare formă încărcată
    print("Loaded shapes:")
    for s in loaded_shapes:
        s.show()
