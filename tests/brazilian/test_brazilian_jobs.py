from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    translation = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in translation:
        assert job.get("titulo") is None
        assert job.get("title") is not None
