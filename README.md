# FastAsync

This project is a minimal viable set used as a proof of concet.
The goal of this project is to try to meet FastAPI, SQLAlchemy, pytest and coverage and make them  work together.


# Install

Required python 3.9 

```shell
pip install -r requirements.txt
```

# Run application

```shell
uvicorn main:app --port 8000
```


# Run tests

```shell
pytest -vv --cov=. --cov-report term-missing
```

