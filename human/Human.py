class Human:
    def __init__(self):
        self.name = "Human"
        print(self.name)


class Action:
    def __init__(self):
        self.name = "Action"
        print(self.name)

    @classmethod
    def action(cls):
        print("action")


class Walk(Action):
    def __init__(self):
        super().__init__()
        self.name = "Walk"
        print(self.name)

    @classmethod
    def action(cls):
        super().action()
        print("walk")


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


class Child(Walk, Woman, Man):
    def __init__(self):
        # super().__init__()
        Walk().__init__()
        self.name = "Child"
        print(self.name)

    def doSomething(self):
        pass


if __name__ == "__main__":
    people = Human()
    people = Woman()
    people = Man()
    people = Child()
    people.action()
