from src.counter import count_ocurrences


def test_counter():
    result = count_ocurrences("src/jobs.csv", "new")
    assert(result == 3221)
