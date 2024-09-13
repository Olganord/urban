class Human:
    def __init__(self, name, age_):
        self.name = name
        self.age_ = age_
        self.say_info()


    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age_}')
    def birthday(self):
        self.age_ += 1
        print(f'У меня день рождения, мне теперь {self.age_}')




den = Human('Denis', 24)
max_ = Human('Max', 22)
max_.birthday()






