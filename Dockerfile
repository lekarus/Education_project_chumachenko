FROM python:3.8

EXPOSE 8000

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv && pipenv install --system

COPY flaskr/ .
COPY run.sh run.sh

# WORKDIR flaskr

RUN chmod a+x run.sh

CMD ["./run.sh"]
