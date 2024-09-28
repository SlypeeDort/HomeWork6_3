class Horse:
    def __init__(self):
        self.dx = None
        self.x_distance = 0
        self.y_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.dx = dx
        self.x_distance = self.x_distance + self.dx


class Eagle:
    def __init__(self):
        self.dy = None
        self.y_distance = None
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.dy = dy
        self.y_distance = self.y_distance + self.dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        print(self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

p1.get_pos()
p1.move(10, 15)
p1.get_pos()
p1.move(-5, 20)
p1.get_pos()

p1.voice()
