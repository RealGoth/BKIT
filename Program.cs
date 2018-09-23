using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    class Program
    {
        static void Main(string[] args)
        {
            double a, b, c;
            Console.WriteLine("\t\t\t===Решение квадратного уравнения===");


            Console.Write("Введите коэффициент A: ");
            while (double.TryParse(Console.ReadLine(), out a) == false)
            {
                Console.WriteLine("Ошибка. Повторите ввод.");
            }

            Console.Write("Введите коэффициент B: ");
            while (double.TryParse(Console.ReadLine(), out b) == false)
            {
                Console.WriteLine("Ошибка. Повторите ввод.");
            }

            Console.Write("Введите коэффициент C: ");
            while (double.TryParse(Console.ReadLine(), out c) == false)
            {
                Console.WriteLine("Ошибка. Повторите ввод.");
            }

            Console.WriteLine("Исходное уравнение: {0}x^2 + {1}x + {2} = 0", a, b, c);

            double d, x1, x2;
            d = b * b - 4 * a * c;
            Console.WriteLine("Дискриминант D = " + d);
            if (d > 0)
            {
                x1 = ((-b) + Math.Sqrt(d)) / (2 * a);
                x2 = ((-b) - Math.Sqrt(d)) / (2 * a);
                Console.WriteLine("Уравнение имеет 2 различных корня:");
                Console.WriteLine("x1 = " + x1);
                Console.WriteLine("x2 = " + x2);
            }
            if (d == 0)
            {
                x1 = (-b) / (2 * a);
                Console.WriteLine("Уравнение имеет 2 совпадающих корня:");
                Console.WriteLine("x1,2 = " + x1);
            }
            if (d < 0)
            {
                Console.WriteLine("Уравнение не имеет действительных корней.\nКоплексные корни:");
                double sqrtD = Math.Sqrt(-d) / (2 * a);
                x1 = (-b) / (2 * a);
                Console.WriteLine("x1 = " + x1 + " +" + sqrtD + "i");
                Console.WriteLine("x2 = " + x1 + " -" + sqrtD + "i");
            }
            Console.ReadKey();
        }
    }
}
