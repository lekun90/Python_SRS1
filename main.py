# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
# проверяет, является ли этот день выходным.
d = int(input('Введите цифрой день недели (от 1 до 7): '))
if (6 <= d <= 7):
    print('Выходной')
elif (0 < d < 6):
    print('Невыходной')
else:
    print('Число не в пределов 7 дней')

# 7.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для
# всех значений предикат.
xyz = ["X", "Y", "Z"]
some_list = []
for i in range(3):
    some_list.append(input(f"Введите значение {xyz[i]}: "))
left = not (some_list[0] or some_list[1] or some_list[2])
right = not some_list[0] and not some_list[1] and not some_list[2]
result = left == right
if result == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")

# 8. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта
# точка (или на какой оси она находится).
xy = ["x", "Y"]
some_list = []
for i in range(2):
    some_list.append(int(input(f"Введите значение координаты {xy[i]}: ")))
text = 4
if some_list[0] > 0 and some_list[1] > 0:
    text = 1
elif some_list[0] < 0 and some_list[1] > 0:
    text = 2
elif some_list[0] < 0 and some_list[1] < 0:
    text = 3
print (f"Точка находится в {text} четверти плоскости")

# 9. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).
num_chet = int(input("Введите четверть: "))
if num_chet == 1:
    print("x>0 и y>0")
elif num_chet == 2:
    print("x<0 и y>0")
elif num_chet == 3:
    print("x<0 и y<0")
elif num_chet == 4:
    print("x>0 и y<0")

# 10. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
xA, yA = map(int, input("Введите через пробел значение координат точки А: ").split())
xB, yB = map(int, input("Введите через пробел значение координат точки B: ").split())
lengthSegment = ((xA - xB) ** 2 + (yA - yB) ** 2) ** 0.5
print(f"Длина отрезка: {format(lengthSegment, '.2f')} ")

