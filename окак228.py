print("Здалова, я лавака сатурнита этот калькулятор именно для тебя")
print("ты крутой?")
x = input()
while x == "да":
    print("выбери действие: умножение, деление, деление на цело, остаток от деления, сложение, вычитание, возведение в степень, квадратный корень и анализ числа")
    try:
        y = str(input())
    except:
        print("Это не слово!")
        break
    if y == "анализ числа":
        print("введи число которое хочешь анализировать")
        try:
            c = int(input())
        except:
            print("Это не число!")
            break
        r = len(str(c))
        print(f"в твоем числе {r} разряда(ов).")
        if c % 2 == 0:
            print("твое число четное")
        else:
            print("твое число не четное")
        su = 0
        for i in str(c):
            su += int(i)
        print(f"сумма всех чисел в твоем числе = {su}")
        k = c ** 0.5
        print(f"квадратный корень твоего числа = {k}")
        kub = c ** 0.33
        print(f"кубический корень твоего числа = {kub}")
        total = 0
        for i in range(1, 10):
            if c % i == 0:
                total += 1
        if total == 2:
            print("твое число простое")
        else:
            print("твое число не простое")
        print("количество какого числа ты хочешь найти в этом числе")
        try:
            kol = int(input())
        except:
            print("Это не число!")
            break
        tot = 0
        for i in str(c):
            if kol == int(i):
                tot += 1
        print(f"в твоем числе таких цифр {tot}")
        break
    elif y == "умножение":
        print("введи два числа которые хочешь умножить")
        try:
            z = int(input())
            c = int(input())
        except:
            print("Это не число!")
            break
        total = z * c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
    elif y == "деление":
        print("введи два числа которые хочешь поделить")
        try:
            z = int(input())
            c = int(input())
        except:
            print("Это не число!")
            break
        total = z / c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
    elif y == "деление на цело":
        print("введи два числа которые хочешь поделить")
        try:
            z = int(input())
            c = int(input())
        except:
            print("Это не число!")
            break
        total = z // c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
    elif y == "остаток от деления":
        print("введи два числа которые хочешь поделить")
        try:
            z = int(input())
            c = int(input())
        except:
            print("Это не число!")
            break
        total = z % c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
    elif y == "сложение":
        print("введи два числа которые хочешь сложить")
        try:
            z = int(input())
            c = int(input())
        except:
            print("Это не число!")
            break
        total = z + c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
    elif y == "вычитание":
        print("введи два числа которые хочешь вычисть")
        try:
            z = int(input())
            c = int(input())
        except:
            print("Это не число!")
            break
        total = z - c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
    elif y == "возведение в степень":
        print("введи число и степень в которую хотите возвести")
        try:
            z = int(input())
            c = int(input())
        except:
            print("Это не число!")
            break
        total = z ** c
        print(total)
        print("хочешь продолжить с этим число, да или нет")
    elif y == "квадратный корень":
        print("введи число из которого ты хочешь найти корень")
        try:
            z = int(input())
        except:
            print("Это не число!")
            break
        total = z ** 0.5
        print(total)
        print("хочешь продолжить с этим число, да или нет")
    try:
        v = str(input())
    except:
        print("Это не слово!")
    while v == "да":
        print("выбери действие: умножение, деление, деление на цело, остаток от деления, сложение, вычитание, возведение в степень")
        try:
            y = str(input())
        except:
            print("Это не слово!")
        if y == "умножение":
            print("введи число на которое хочешь домножить это")
            try:
                c = int(input())
            except:
                print("Это не число!")
                break
            total = total * c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            try:
                v = str(input())
            except:
                print("Это не слово!")
        if y == "деление":
            print("введи число на которое хочешь поделить это")
            try:
                c = int(input())
            except:
                print("Это не число!")
                break
            total = total / c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            try:
                v = str(input())
            except:
                print("Это не слово!")
        if y == "деление на цело":
            print("введи число на которое хочешь поделить это")
            try:
                c = int(input())
            except:
                print("Это не число!")
                break
            total = total // c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            try:
                v = str(input())
            except:
                print("Это не слово!")
        if y == "остаток от деления":
            print("введи число на которое хочешь поделить это")
            try:
                c = int(input())
            except:
                print("Это не число!")
                break
            total = total % c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            try:
                v = str(input())
            except:
                print("Это не слово!")
        if y == "сложение":
            print("введи число которое хочешь прибавить это")
            try:
                c = int(input())
            except:
                print("Это не число!")
            break
            total = total + c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            try:
                v = str(input())
            except:
                print("Это не слово!")
        if y == "вычитание":
            print("введи число которое хочешь вычисть это")
            try:
                c = int(input())
            except:
                print("Это не число!")
                break
            total = total - c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            try:
                v = str(input())
            except:
                print("Это не слово!")
        if y == "возведение в степень":
            print("введи степень в которую хотите возвести число")
            try:
                c = int(input())
            except:
                print("Это не число!")
                break
            total = total ** c
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            try:
                v = str(input())
            except:
                print("Это не слово!")
        if y == "квадратный корень":
            total = total ** 0.5
            print(total)
            print("хочешь продолжить с этим число, да или нет")
            try:
                v = str(input())
            except:
                print("Это не слово!")
        if v == "нет":
            print("закончить работу с калькулятором?")
            try:
                e = str(input())
            except:
                print("Это не слово!")
                break
    if e == "да":
        break
if x == "нет":
    print("ты не дидиблад, тебе это калькулятор не нужен((((")
elif x != "да":
    print("тебе это калькулятор не нужен((((")
elif x == "да":
    print(total)
elif x == "да" and y == "нализ числа":
    print("до новых встречь, пока))")
