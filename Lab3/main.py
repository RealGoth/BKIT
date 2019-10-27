from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle(3, 2, 'красного')
    s = Square(5, 'синего')
    c = Circle(5, 'фиолетового')


    print(r)
    print(s)
    print(c)


if __name__ == '__main__':
    main()
