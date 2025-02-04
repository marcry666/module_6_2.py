class Vehicle:

    __COLOR_VARIANTS = ["black", "white", "red", "grey", "green", "blue"]

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5
    
    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

vehicle1 = Sedan('Fedos', 'Porsche 911', 329, 'blue')
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Peter'

vehicle1.print_info()