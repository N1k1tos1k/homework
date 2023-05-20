class Worker:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def Show(self):
        print("Cотрудник по имени ", self.name, ", ", self.age, " лет, и зарплата в ", self.money, " рублей.")

worker1 = Worker("Никита",18, 150000)
worker1.Show()