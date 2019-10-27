from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):

    FIGURE_TYPE = 'Круг'

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, rad_param, color_param):
        self.radius = rad_param
        self.fc = FigureColor()
        self.fc.color = color_param

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return '{} {} цвета с радиусом {} площадью {}'.format(
            Circle.get_figure_type(),
            self.fc.color,
            self.radius,
            self.area()
        )
