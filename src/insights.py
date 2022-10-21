from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_type = set()
    for job in jobs_list:
        job_type.add(job["job_type"])
    return list(job_type)


def filter_by_job_type(jobs, job_type):
    jobs_list = list()
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)
    return (jobs_list)


def get_unique_industries(path):
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    jobs_list = list()
    for job in jobs:
        if job["industry"] == industry:
            jobs_list.append(job)
    return (jobs_list)


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = []
    for job in jobs_list:
        if job["max_salary"].isnumeric():
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = []
    for job in jobs_list:
        if job["min_salary"].isnumeric():
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        job.get("min_salary") is None
        or job.get("max_salary") is None
        or type(job.get("min_salary")) is not int
        or type(job.get("max_salary")) is not int
        or job.get("min_salary") > job.get("max_salary")
        or type(salary) is not int
    ):
        raise ValueError("Invalid input")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    list_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_salary.append(job)
        except ValueError:
            print("Invalid input")
    return list_salary
