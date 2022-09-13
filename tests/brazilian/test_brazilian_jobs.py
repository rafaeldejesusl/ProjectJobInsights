from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    example = {"title": "Maquinista", "salary": "2000", "type": "trainee"}
    for item in result:
        assert(example.keys() == item.keys())
