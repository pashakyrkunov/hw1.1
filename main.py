# distance - расстояние, которое нужно пробежать
def while_task1(distance):
    power = 0
    days = 0
    while distance > 0:
        distance = distance - (2 ** power)
        power += 1
        days += 1
        return days


print(while_task1(1000))
print(while_task1(10000))


# days - кол-во дней всего
# dist - расстояние за первый день
def while_task3(days, dist):
    ans = 10
    i = 1
    while i < days:
        if i % 2 == 0:
            dist *= 1.15
        ans += dist
        i += 1
    return ans


print(while_task3(30, 10))


# dist - дистанция в первый день пробежки
# dist_goal - дистанция-цель за день
def while_task4a(dist, dist_goal):
    days = 1
    while dist <= dist_goal:
        dist *= 1.1
        days += 1
    return days


print(while_task4a(10, 20))


# dist - дистанция в первый день пробежки
# total - суммарный путь, который нужно пробежать
def while_task4b(dist, total):
    days = 1
    sum_dist = dist
    while sum_dist < total:
        dist *= 1.1
        sum_dist += dist
        days += 1
    return days


print(while_task4b(10, 100))


# n - номер элемента последовательности, который нужно вывести
def for_task1(n):
    sequence = [1, 1]
    for i in range(2, n):
        element = sequence[i - 1] + sequence[i - 2]
        sequence.append(element)
    return element


print(for_task1(10))


# n - номер элемента последовательности, который нужно вывести
def for_task2(n):
    sequence = [1, 1, 1]
    for i in range(3, n):
        element = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        sequence.append(element)
    return element


print(for_task2(6))


# n - конечный элемент(вывод квадратов чисел до n)
def for_task3(n):
    list1 = [i ** 2 for i in range(0, n) if i % 2 != 0]
    return list1


print(for_task3(8))


# a, b - рендж чисел
def for_task4(a, b):
    total = 0
    prod = a
    for i in range(a, b):
        total += i
        prod *= i
    print("sum = " + str(total))
    print("production = " + str(prod))


for_task4(4, 9)


# a, b - рендж чисел
def for_task5(a, b):
    even_nums = [i for i in range(a, b) if i % 2 == 0]
    odd_nums = [i for i in range(a, b) if i % 2 != 0]

    print(even_nums)
    print(odd_nums)


for_task5(1, 10)


# given_list - исходный список чисел
def for_task6(given_list):
    positive_nums = [i for i in given_list if i >= 0]
    negative_nums = [i for i in given_list if i < 0]

    print(positive_nums)
    print(negative_nums)


for_task6([-14, 13, 2, -3231, 5, 200])


# h - высота фигуры
# w - ширина
# symbol - символ
def draw_task2(h, w, symbol):
    if h > 1 and w > 1:
        for i in range(0, w):
            if i == 0 or i == w - 1:
                print(h * symbol)
            else:
                print(symbol + (h - 2) * ' ' + symbol)
    else:
        print('Incorrect arguments')


print("Задание 2")
draw_task2(5, 5, '#')


# h - высота фигуры
# w - ширина
# f - толщина
# symbol - символ
def draw_task3(h, w, f, symbol):
    if h > 1 and w > 1 and 2 * f <= min(h, w):
        for i in range(1, w + 1):
            if i <= f or i > w - f:
                print(h * symbol)
            else:
                print(f * symbol + (h - 2 * f) * ' ' + f * symbol)
    else:
        print('Incorrect arguments')


print("Задание 3")
draw_task3(4, 12, 1, "#")
draw_task3(25, 8, 2, "№")
