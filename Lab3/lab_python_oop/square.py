from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):

    FIGURE_TYPE = 'Квадрат'

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, side_param, color_param):
        self.side = side_param
        super().__init__(side_param, side_param, color_param)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}'.format(
            Square.get_figure_type(),
            self.fc.color,
            self.side,
            self.area()
        )
