class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def about_dog(self):
        print("Собаку зовут {}, ее порода - {}. Ее возраст - {}".format(self.name, self.breed, self.age))


my_dog = Dog("Шарик", 2, "лабрадор")
my_dog.about_dog()