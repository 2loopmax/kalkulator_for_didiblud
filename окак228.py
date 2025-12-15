print("Здалова дидиблад я лавака сатурнита этот калькулятор именно для тебя")
print("ты дидиблад?")
x = input()
while x == "да" or e != "да":
    print("выбери действие: умножение, деление, деление на цело, остаток от деления, сложение, вычитание, возведение в степень, квадратный корень и анализ числа")
    y = input()
    if y == "анализ числа":
        print("введи число которое хочешь анализировать")
        c = int(input())
        
    elif y == "умножение":
        print("введи два числа которые хочешь умножить")
        z = int(input())
        c = int(input())
        if 1 not in z and 2 not in z and 3 not in z and 4 not in z and 5 not in z and 6 not in z and 7 not in z and 8 not in z and 9 not in z:
            break
        if 1 not in c and 2 not in c and 3 not in c and 4 not in c and 5 not in c and 6 not in c and 7 not in c and 8 not in c and 9 not in c:
            break
        total = z * c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
        v = input()
    elif y == "деление":
        print("введи два числа которые хочешь поделить")
        z = int(input())
        c = int(input())
        total = z / c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
        v = input()
    elif y == "деление на цело":
        print("введи два числа которые хочешь поделить")
        z = int(input())
        c = int(input())
        total = z // c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
        v = input()
    elif y == "остаток от деления":
        print("введи два числа которые хочешь поделить")
        z = int(input())
        c = int(input())
        total = z % c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
        v = input()
    elif y == "сложение":
        print("введи два числа которые хочешь сложить")
        z = int(input())
        c = int(input())
        total = z + c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
        v = input()
    elif y == "вычитание":
        print("введи два числа которые хочешь вычисть")
        z = int(input())
        c = int(input())
        total = z - c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
        v = input()
    elif y == "возведение в степень":
        print("введи число и степень в которую хотите возвести")
        z = int(input())
        c = int(input())
        total = z ** c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
        v = input()
    elif y == "квадратный корень":
        print("введи число из которого ты хочешь найти корень")
        z = int(input())
        total = z ** 0.5
        print(total)
        print("хочешь продолжить с этим число, да или нет")
        v = input()
    else:
        lf = 67
        print(lf)
        break
    print(total)
    while v == "да":
        print("выбери действие: умножение, деление, деление на цело, остаток от деления, сложение, вычитание, возведение в степень")
        y = input()
        if y == "умножение":
            print("введи число на которое хочешь домножить это")
            c = int(input())
            total = total * c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            v = input()
        if y == "деление":
            print("введи число на которое хочешь поделить это")
            c = int(input())
            total = total / c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            v = input()
        if y == "деление на цело":
            print("введи число на которое хочешь поделить это")
            c = int(input())
            total = total // c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            v = input()
        if y == "остаток от деления":
            print("введи число на которое хочешь поделить это")
            c = int(input())
            total = total % c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            v = input()
        if y == "сложение":
            print("введи число которое хочешь прибавить это")
            c = int(input())
            total = total + c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            v = input()
        if y == "вычитание":
            print("в5веди число которое хочешь вычисть это")
            c = int(input())
            total = total - c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            v = input()
        if y == "возведение в степень":
            print("введи степень в которую хотите возвести число")
            c = int(input())
            total = total ** c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            v = input()
        if y == "квадратный корень":
            total = total ** 0.5
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            v = input()
            if v == "нет":
                print("закончить работу с калькулятором?")
                e = input()
        else:
            lf = 67
            print(lf)
            break
    if lf == 67:
        break
    if e == "да":
        break
if x == "нет":
    print("ты не дидиблад, тебе это калькулятор не нужен((((")
elif lf == 67:
    for i in range(66):
        print(67)
elif x != "да":
    print("тебе это калькулятор не нужен((((")
elif x == "да":
    print(total)
