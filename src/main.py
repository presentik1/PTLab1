# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from PerfectScorer import PerfectScorer  # Импортируем PerfectScorer

# Функция для получения пути из аргументов командной строки
def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p", dest="path", type=str, required=True,
        help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path

def main():
    # Получаем путь к файлу данных
    path = get_path_from_arguments(sys.argv[1:])

    # Чтение данных
    reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)

    # Вычисляем рейтинг студентов
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    # Ищем студентов с 100 баллами по всем дисциплинам
    scorer = PerfectScorer(students)  # Создаем объект PerfectScorer
    perfect_student = scorer.find_perfect_student()  # Находим такого студента

    # Выводим результат
    print(perfect_student)

if __name__ == "__main__":
    main()
