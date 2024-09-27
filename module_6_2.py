from colorama import Fore


class Vehicle:  # подкласс Sedan
    __COLOR_VARIANTS = ['yellow', 'purple', 'black']

    def __init__(self, owner, _model, _engine_power, _color):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color

    def get_model(self):
        return Fore.BLUE + f'Модель: {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self._color = new_color
        else:
            print(Fore.MAGENTA + 'Нельзя сменить цвет на ' + f'{new_color}')

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    # __PASSENGERS_LIMIT = 5 # атрибут не используется
        pass

# Текущие цвета __COLOR_VARIANTS = ['yellow', 'purple', 'black']
vehicle1 = Sedan(Fore.BLUE + 'Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч., вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = Fore.GREEN + 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

