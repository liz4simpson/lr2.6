#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import datetime

if __name__ == '__main__':
    # Список поездов
    trains = []
    while True:
        # Запрос команды из терминала
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            # Запрос данных о поездке
            name = input("Пункт назначения: ")
            number = input("Номер поезда: ")
            time_str = input("Время отправления: (hh:mm) ")
            time = datetime.datetime.strptime(time_str, '%H:%M').time()
            # Создаем словарь
            train = {
                'name': name,
                'number': number,
                'time': time,
            }
            # Добавили словарь в список
            trains.append(train)
            if len(trains) > 1:
                # Сортировка
                trains.sort(key=lambda item: item.get('time', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Пункт назначения",
                    "Номер поезда",
                    "Время отправления"
                )
            )
            print(line)
            # Вывод данных о всех поездах
            for idx, train in enumerate(trains, 1):
                time = train.get('time', '')
                print(
                    '| {:>4} | {:<30} | {:<20} | {}{:>12} |'.format(
                        idx,
                        train.get('name', ''),
                        train.get('number', ''),
                        time,
                        ' ' * 5
                    )
                )
            print(line)

        elif command.startswith('select'):
            print("Введите название пункта назначения: ")
            p_n = input()
            count = 0
            # Проверка сведений из списка
            for train in trains:
                if train.get('name') == p_n:
                    count += 1
                    print('Пункт назначения:', train.get('name', ''))
                    print('Номер поезда:', train.get('number', ''))
                    print('Время отправления:', train.get('time', ''))

            if count == 0:
                print("Таких поездов нет!")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select найти информацию о поезде по номеру")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
