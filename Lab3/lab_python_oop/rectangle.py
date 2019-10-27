from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):

    FIGURE_TYPE = 'Прямоугольник'

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width_param, height_param, color_param):
        self.width = width_param
        self.height = height_param
        self.fc = FigureColor()
        self.fc.color = color_param

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета с шириной {} и высотой {} площадью {}'.format(
            Rectangle.get_figure_type(),
            self.fc.color,
            self.width,
            self.height,
            self.area()
        )
