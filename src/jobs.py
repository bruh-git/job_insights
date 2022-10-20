from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open("jobs.csv") as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for linha in reader:
            print(linha)
