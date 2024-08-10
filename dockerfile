FROM python:3.10

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install

COPY . /app

EXPOSE 8000

RUN pipenv run pip install fastapi[all]

CMD ["pipenv", "run", "fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]