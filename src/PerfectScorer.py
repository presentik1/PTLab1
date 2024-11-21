from Types import DataType


class PerfectScorer:
    def __init__(self, data: DataType):
        self.data = data

    def find_perfect_student(self):
        for student, subjects in self.data.items():
            if all(score == 100 for _, score in subjects):
                return f"Студент {student} имеет 100 баллов по всем дисциплинам."
        return "Нет студентов, имеющих 100 баллов по всем дисциплинам."
