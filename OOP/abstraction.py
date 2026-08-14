class Car:
    def __init__(self):
        self.accelerator=False
        self.brake=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.aacelarator=True
        print("Car Started.......")

C=Car()
C.start()