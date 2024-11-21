from src.PerfectScorer import PerfectScorer
from src.Types import DataType

def test_find_perfect_student():
    data: DataType = {
        "Иванов Иван": [("математика", 100), ("литература", 100)],
        "Петров Петр": [("химия", 80), ("физика", 60)],
    }
    scorer = PerfectScorer(data)
    result = scorer.find_perfect_student()
    assert result == "Студент Иванов Иван имеет 100 баллов по всем дисциплинам."

def test_no_perfect_students():
    data: DataType = {
        "Иванов Иван": [("математика", 100), ("литература", 90)],
        "Петров Петр": [("химия", 80), ("физика", 60)],
    }
    scorer = PerfectScorer(data)
    result = scorer.find_perfect_student()
    assert result == "Нет студентов, имеющих 100 баллов по всем дисциплинам."
