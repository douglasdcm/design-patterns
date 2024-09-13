# Interface. THe Leaf classes don't need to implement the "add", "remove" because they are
# part of the Composite class
# Grafic is the Component
class Grafic:
    def draw(self):
        raise NotImplementedError

    def add(self, grafic):
        raise NotImplementedError

    def remove(self, grafic):
        raise NotImplementedError

    def get_children(self, i: int):
        raise NotImplementedError


# Leaf
class Line(Grafic):
    def draw(self):
        return "draw line"


# Leaf
class Rectange(Grafic):
    def draw(self):
        return "draw rectangle"


# Leaf
class Text(Grafic):
    def draw(self):
        return "draw text"


# Composite. Notice it is a subclass of Component too
class Picture(Grafic):
    grafics: list[Grafic] = []

    def draw(self):
        # Not part of the original code. Added to enable the inpection in tests
        result = []
        # Excutes the function for its children
        for g in self.grafics:
            r = g.draw()
            result.append(r)  # added for inspection
        return result

    def add(self, grafic: Grafic):
        self.grafics.append(grafic)

    def remove(self, grafic):
        self.grafics.remove(grafic)

    def get_children(self, i: int):
        return self.grafics[i]


def client():
    line: Grafic = Line()
    text: Grafic = Text()
    picture: Grafic = Picture()
    picture.add(line)
    picture.add(text)
    # raises NotImplemtedError as a Leaf does not have children
    # line.add(text)
    return picture, line
