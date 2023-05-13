class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print("кошку зовут {}, {} лет, цвет {}".format(self.name, self.age, self.color))


my_cat = Cat("Пушок", 6, "белый")
my_cat.info()