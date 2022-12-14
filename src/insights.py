from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    data = read(path)
    group_by_types = {}
    for row in data:
        type = row["job_type"]
        if type not in group_by_types:
            group_by_types[type] = 0
        group_by_types[type] += 1
    return group_by_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    job_types_filtered = []
    for row in jobs:
        type = row["job_type"]
        if type == job_type:
            job_types_filtered.append(row)
    return job_types_filtered


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    data = read(path)
    group_by_industries = {}
    for row in data:
        industry = row["industry"]
        if industry == "":
            continue
        if industry not in group_by_industries:
            group_by_industries[industry] = 0
        group_by_industries[industry] += 1
    return group_by_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    job_industry_filtered = []
    for row in jobs:
        job_industry = row["industry"]
        if industry == job_industry:
            job_industry_filtered.append(row)
    return job_industry_filtered


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = read(path)
    list_max_salary = []
    for row in data:
        max_salary = row["max_salary"]
        if max_salary != "" and max_salary.isnumeric():
            list_max_salary.append(int(max_salary))
    max_salary = max(list_max_salary)
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = read(path)
    list_min_salary = []
    for row in data:
        min_salary = row["min_salary"]
        if min_salary != "" and min_salary.isnumeric():
            list_min_salary.append(int(min_salary))
    min_salary = min(list_min_salary)
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    check = False
    try:
        max_salary = job["max_salary"]
        min_salary = job["min_salary"]
    except KeyError:
        raise ValueError()
    if (not str(max_salary).isnumeric() or not str(min_salary).isnumeric() or
            max_salary < min_salary or not isinstance(salary, int)):
        raise ValueError()
    if int(min_salary) <= int(salary) <= int(max_salary):
        check = True
    return check


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    job_salary_filtered = []
    for row in jobs:
        try:
            if matches_salary_range(row, salary):
                job_salary_filtered.append(row)
        except ValueError:
            pass
    return job_salary_filtered
