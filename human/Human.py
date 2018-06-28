class Human:
    def __init__(self):
        self.name = "Human"
        print(self.name)


class Woman(Human):
    def __init__(self):
        super().__init__()
        self.name = "Woman"
        print(self.name)


class Man(Human):
    def __init__(self):
        super().__init__()
        self.name = "Man"
        print(self.name)


class Child(Man, Woman):
    def __init__(self):
        super().__init__()
        self.name = "Child"
        print(self.name)


if __name__ == "__main__":
    people = Human()
    people = Woman()
    people = Man()
    people = Child()
