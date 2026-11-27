import json
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Question:
    """Модель вопроса с вариантами ответа."""
    text: str
    options: list[str]
    correct_index: int

    def __post_init__(self) -> None:
        if not self.text or not self.text.strip():
            raise ValueError("Текст вопроса не может быть пустым.")
        if len(self.options) < 2:
            raise ValueError("У вопроса должно быть минимум 2 варианта ответа.")
        if not (0 <= self.correct_index < len(self.options)):
            raise ValueError("Индекс правильного ответа вне диапазона.")


class QuizEngine:
    """Модуль тестирования знаний: банк вопросов, прохождение и история."""

    def __init__(self) -> None:
        self._questions: list[Question] = []
        self._history: list[dict] = []

    @property
    def questions(self) -> list[Question]:
        return list(self._questions)

    @property
    def history(self) -> list[dict]:
        return list(self._history)

    def add_question(self, question: Question) -> None:
        if not isinstance(question, Question):
            raise TypeError("Ожидается объект класса Question.")
        self._questions.append(question)

    def remove_question(self, index: int) -> Question:
        if not (0 <= index < len(self._questions)):
            raise IndexError("Вопрос с таким индексом не найден.")
        return self._questions.pop(index)

    @staticmethod
    def calculate_grade(percent: float) -> int:
        if percent >= 90:
            return 5
        if percent >= 75:
            return 4
        if percent >= 60:
            return 3
        return 2

    def take_quiz(self, student_name: str, answers: list[int]) -> dict:
        if not student_name or not student_name.strip():
            raise ValueError("Имя тестируемого не может быть пустым.")
        if not self._questions:
            raise ValueError("Банк вопросов пуст.")
        if len(answers) != len(self._questions):
            raise ValueError("Количество ответов не совпадает с числом вопросов.")

        score: int = 0
        for q, ans in zip(self._questions, answers):
            if not (0 <= ans < len(q.options)):
                raise ValueError("Выбран несуществующий вариант ответа.")
            if ans == q.correct_index:
                score += 1

        total = len(self._questions)
        percent = round(score / total * 100, 1)
        record = {
            "student": student_name.strip(),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "score": score,
            "total": total,
            "percent": percent,
            "grade": self.calculate_grade(percent),
        }
        self._history.append(record)
        return record

    def save_history(self, filepath: str) -> None:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self._history, f, ensure_ascii=False, indent=2)

    def load_history(self, filepath: str) -> list[dict]:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Некорректный формат файла истории.")
        self._history = data
        return self.history
