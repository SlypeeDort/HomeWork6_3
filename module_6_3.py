class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)


    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return print(self.x_distance, self.y_distance)

    def voice(self):
        print(Eagle.sound)


p1 = Pegasus()

p1.get_pos()
p1.move(10, 15)
p1.get_pos()
p1.move(-5, 20)
p1.get_pos()

p1.voice()
