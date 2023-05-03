from copy import copy
import numpy as np
from random import randint


class Exercises:
    @staticmethod
    def ex_1(numbers: str) -> str:
        try:
            test_list, result_list = [], []
            for array in np.array_split([int(x) for x in numbers.split(' ')], 3):
                test_list.append(list(array))
            if np.mean(test_list[0] + test_list[1]) > 0:
                first_two_thirds = test_list[0] + test_list[1]
                first_two_thirds.sort()
                result_list.append(', '.join([str(x) for x in (first_two_thirds + test_list[2][::-1])]))
                return ', '.join(result_list)
            else:
                first_one_third = test_list[0]
                first_one_third.sort()
                result_list.append(', '.join([str(x) for x in (first_one_third + (test_list[1] + test_list[2])[::-1])]))
                return ', '.join(result_list)

        except ValueError:
            return 'Ошибка ввода. Введите числа заново.'

    @staticmethod
    def ex_2(form_data: dict) -> dict:
        try:
            # ПЕРЕМЕННЫЕ
            estimates_list: list = [int(x) for x in form_data['estimates'].split(' ')]
            number_of_estimate: int = int(form_data['number_of_estimate'])
            new_estimate: int = int(form_data['new_estimate'])
            sort: str = form_data['sort']
            average_estimate: int = sum(estimates_list) / 10
            result_dict: dict = {}

            # ГЛАВНАЯ ПРОВЕРКА НА КОЛИЧЕСТВО ВВЕДЕННЫХ ОЦЕНОК
            if len(estimates_list) == 10:

                # ПРОВЕРКА КАЖДОЙ ОЦЕНКИ НА СООТВЕТСТВИЕ ШКАЛЕ ОЦЕНОК
                for number in estimates_list:
                    if number < 1 or number > 12:
                        return {'error': 'Ошибка ввода. Диапазон оценок от 1 до 12.'}

                # ПРОВЕРКА НОМЕРА ЗАМЕНЯЕМОЙ ОЦЕНКИ НА СООТВЕТСТВИЕ ДИАПАЗОНУ КОЛИЧЕСТВА ОЦЕНОК
                if number_of_estimate < 1 or number_of_estimate > 10:
                    return {'error': 'Ошибка ввода. Максимальное количество оценок — 10. Введен несуществующий '
                                     'индекс.'}

                # ПРОВЕРКА НОВОЙ ОЦЕНКИ НА СООТВЕТСТВИЕ ШКАЛЕ ОЦЕНОК
                if new_estimate < 1 or new_estimate > 12:
                    return {'error': 'Ошибка ввода. Диапазон оценок от 1 до 12.'}

                # СОЗДАНИЕ КОПИИ СПИСКА ОЦЕНОК И ЗАМЕНА НУЖНОГО НОМЕРА ОЦЕНКИ НА НОВУЮ ОЦЕНКУ
                new_estimates_list = copy(estimates_list)
                new_estimates_list[number_of_estimate] = new_estimate

                # ДОБАВЛЕНИЕ В ИТОГОВЫЙ СЛОВАРЬ РЕЗУЛЬТАТОВ
                result_dict['estimates'] = 'Изначальные оценки студента -> ' + ', '.join(str(x) for x in estimates_list)
                result_dict['new_estimates'] = 'Оценки студента после пересдачи -> ' + ', '.join(
                    str(x) for x in new_estimates_list)

                # ВЫБОР СОРТИРОВКИ И ДОБАВЛЕНИЕ НУЖНОЙ В ИТОГОВЫЙ СЛОВАРЬ
                if sort == 'sort_ascending':
                    new_estimates_list.sort()
                    result_dict[
                        'sorted'] = 'Выбрана сортировка по возрастанию -> ' + f'{", ".join([str(x) for x in new_estimates_list])}'
                else:
                    new_estimates_list.sort(reverse=True)
                    result_dict[
                        'sorted'] = 'Выбрана сортировка по убыванию -> ' + f'{", ".join([str(x) for x in new_estimates_list])}'
            # ЕСЛИ КОЛИЧЕСТВО ВВЕДЕННЫХ ОЦЕНОК НЕ СООТВЕТСТВУЕТ - ВЫДАЕТ ОШИБКУ
            else:
                return {'error': 'Ошибка ввода. Введите 10 чисел.'}

            # ПРОВЕРКА НА ТО, БУДЕТ ЛИ СТИПЕНДИЯ У СТУДЕНТА, РЕЗУЛЬТАТ ДОБАВЛЯЕМ В ИТОГОВЫЙ СЛОВАРЬ
            if average_estimate >= 10.7:
                scholarship = 'У этого студента выходит стипендия, так как средний балл не ниже 10.7.'
                result_dict['scholarship'] = scholarship
            else:
                scholarship = 'У этого студента не будет стипендии, так как средний балл оказался ниже 10.7.'
                result_dict['scholarship'] = scholarship

            # В КОНЦЕ ВОЗВРАЩАЕМ ИТОГОВЫЙ СЛОВАРЬ СО ВСЕМИ ДОБАВЛЕННЫМИ КЛЮЧАМИ, ЕСЛИ НЕ ВЫДАЛО НИКАКИХ ОШИБОК
            return result_dict

        except ValueError:
            return {
                'error': 'Ошибка ввода. Заполните форму заново. Возможные причины:',
                'first_reason': '1. Поля ввода пустые.',
                'second_reason': '2. В полях ввода номера оценки и оценки за пересдачу введены по несколько чисел.',
                'third_reason': '3. В полях ввода обнаружены буквы.',
            }

    @staticmethod
    def ex_3(number: str) -> str:
        try:
            if len(number) != 0:
                numbers_list = []
                length_of_list = abs(int(number))
                for _ in range(length_of_list):
                    numbers_list.append(randint(-500, 500))
                for i in range(length_of_list - 1):
                    for j in range(length_of_list - i - 1):
                        if numbers_list[j] > numbers_list[j + 1]:
                            numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
                return ', '.join([str(x) for x in numbers_list])
            else:
                return 'Ошибка. Поле ввода пустое.'
        except ValueError:
            return 'Ошибка ввода. Скорее всего, Вы ввели букву или недопустимый символ. Введите целое число.'
