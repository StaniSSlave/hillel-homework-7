"""
Важливо: не використовувати цикли для реалізації основної логіки.

Потрібно використати рекурсію.

Цикл можна використовувати лише у 4 завданні для знаходження суми чисел.

Завдання 1.

Написати рекурсивну функцію знаходження ступеня числа.

Завдання 2.

Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.

Проілюструйте роботу функції прикладом. (Протестувати)

Завдання 3.

Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.

Користувач вводить a та b. Проілюструйте роботу функції прикладом.

Додатково:

Завдання 4.

Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим чином і знаходить
позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.
"""


task_n = 1

while task_n != 3:
    try:
        task_n = int(input("Select please task number, that you want to check: \n"
                           "\t1. Написати рекурсивну функцію знаходження ступеня числа.\n"
                           "\t2. Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.\n"
                           "\t3. Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b."
                           "\t4. Stop checking tasks\n"
                           "Enter choise here: "))

        match task_n:
            case 1:
                finish_t1_l = "y"
                while finish_t1_l == "y":

                    def exponentiation(number, degree):
                        if degree <= 1:
                            return number

                        return number * exponentiation(number, degree - 1)


                    base_num = int(input("\tEnter here base number, that you want to work with: "))
                    power_num = int(input("\tEnter here power number: "))
                    print(f"\tHere is the result of exponentiation: {exponentiation(base_num, power_num)}")
                    # exponentiation(base_num, power_num) -> base_num * exponentiation(base_num, power_num-1)
                    # exponentiation(base_num, power_num-1) -> base_num * exponentiation(base_num, power_num-2)
                    # ...
                    # exponentiation(base_num, 1) => base_num

                    while finish_t1_l != "y" or finish_t1_l != "n":
                        finish_t1_l = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t1_l = finish_t1_l.lower()
                        try:
                            if finish_t1_l == "y":
                                break
                            elif finish_t1_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 2:
                finish_t2_l = "y"
                while finish_t2_l == "y":

                    def print_stars(number):
                        if number == 1:
                            return "*"

                        return "*" + print_stars(number - 1)

                    number_of_stars = int(input("Enter here number of stars, that you want to see: "))
                    print(print_stars(number_of_stars))

                    # print_stars(number_of_stars) -> "*" + print_stars(number_of_stars-1)
                    # print_stars(number_of_stars-1) -> "*" + print_stars(number_of_stars-2)
                    # ...
                    # print_stars(1) => "*"

                    while finish_t2_l != "y" or finish_t2_l != "n":
                        finish_t2 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t2_l = finish_t2.lower()
                        try:
                            if finish_t2_l == "y":
                                break
                            elif finish_t2_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 3:
                finish_t2_l = "y"
                while finish_t2_l == "y":

                    def sum_of_nums_in_range(num1, num2):


                    first_number, second_munber = int(import("Enter here first number of range: ")), int(import("Enter here second number of range: "))

                    while finish_t2_l != "y" or finish_t2_l != "n":
                        finish_t2 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t2_l = finish_t2.lower()
                        try:
                            if finish_t2_l == "y":
                                break
                            elif finish_t2_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 4:
                print("\tThanks for your time!")
                break
            case _:
                raise Exception("Please enter a valid task number!")
    except ValueError as e:
        print("\tError: Please enter only integers!")
    except Exception as e:
        print(f"\tError: {e}")