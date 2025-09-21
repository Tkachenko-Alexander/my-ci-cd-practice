from app.utils import sum_list


def test_sum_list_empty() -> None:
    assert sum_list([]) == 0


def test_sum_list_positive() -> None:
    assert sum_list([1, 2, 3.5]) == 6.5


def test_sum_list_negative() -> None:
    assert sum_list([-1, 1]) == 0
