# OOP, Class, Class Variable, Methods, Object Variable, Object Variable = istance,
class computer:
    def __init__(self, name, ram, graphic, cpu):
        self.name = name
        self.ram = ram
        self.graphic = graphic
        self.cpu = cpu

    def inf(self):
        print(
            "for %s ram=%i graphic=%i  cpu=%s"
            % (self.name, self.ram, self.graphic, self.cpu)
        )


Dell = computer("dell", 8, 1, "i5")
Dell.inf()
