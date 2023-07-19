
FROM python:3.9-bullseye


WORKDIR /app


COPY ./requirements.txt /app/requirements.txt


RUN pip install  -r /app/requirements.txt


COPY ./app /app


EXPOSE 8000


