import pytest
from quiz_module import Question, QuizEngine


@pytest.fixture
def engine() -> QuizEngine:
    q = QuizEngine()
    q.add_question(Question("Язык Python является:", ["Компилируемым", "Интерпретируемым"], 1))
    q.add_question(Question("Результат 2 ** 3:", ["6", "8", "9"], 1))
    q.add_question(Question("Тип списка в Python:", ["list", "tuple", "dict"], 0))
    return q


def test_add_question(engine):
    assert len(engine.questions) == 3


def test_question_empty_text_raises():
    with pytest.raises(ValueError):
        Question("   ", ["Да", "Нет"], 0)


def test_question_too_few_options_raises():
    with pytest.raises(ValueError):
        Question("Вопрос?", ["Один вариант"], 0)


def test_question_invalid_correct_index_raises():
    with pytest.raises(ValueError):
        Question("Вопрос?", ["A", "B"], 5)


def test_add_invalid_type_raises(engine):
    with pytest.raises(TypeError):
        engine.add_question("не вопрос")  # type: ignore


def test_remove_question_success(engine):
    removed = engine.remove_question(0)
    assert removed.text == "Язык Python является:"
    assert len(engine.questions) == 2


def test_remove_question_out_of_range_raises(engine):
    with pytest.raises(IndexError):
        engine.remove_question(10)


def test_take_quiz_all_correct(engine):
    res = engine.take_quiz("Фархутдинова А.Р.", [1, 1, 0])
    assert res["score"] == 3
    assert res["percent"] == 100.0
    assert res["grade"] == 5
    assert len(engine.history) == 1


def test_take_quiz_partial_score(engine):
    res = engine.take_quiz("Иванов И.И.", [1, 0, 0])
    assert res["score"] == 2
    assert res["percent"] == 66.7
    assert res["grade"] == 3


def test_take_quiz_empty_name_raises(engine):
    with pytest.raises(ValueError):
        engine.take_quiz("", [1, 1, 0])


def test_take_quiz_wrong_answers_count_raises(engine):
    with pytest.raises(ValueError):
        engine.take_quiz("Студент", [1])


def test_save_and_load_history(engine, tmp_path):
    engine.take_quiz("Фархутдинова А.Р.", [1, 1, 0])
    file_path = tmp_path / "history.json"
    engine.save_history(str(file_path))

    new_engine = QuizEngine()
    loaded = new_engine.load_history(str(file_path))
    assert len(loaded) == 1
    assert loaded[0]["student"] == "Фархутдинова А.Р."
    assert loaded[0]["grade"] == 5
