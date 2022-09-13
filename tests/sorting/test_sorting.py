from operator import itemgetter
from src.sorting import sort_by

dic_moq = [
    {"min_salary": 3000, "max_salary": 3500, "date_posted": "2022-09-12"},
    {"min_salary": 5000, "max_salary": 7000, "date_posted": "2021-08-22"}]


def test_sort_by_criteria():
    sort_by(dic_moq, "max_salary")
    newlist = list(dic_moq)
    expected1 = sorted(newlist, key=itemgetter("max_salary"), reverse=True)
    assert(expected1 == dic_moq)
    sort_by(dic_moq, "min_salary")
    expected2 = sorted(newlist, key=itemgetter("min_salary"), reverse=False)
    assert(expected2 == dic_moq)
    sort_by(dic_moq, "date_posted")
    expected3 = sorted(newlist, key=itemgetter("date_posted"), reverse=True)
    assert(expected3 == dic_moq)
