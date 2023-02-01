FROM python:3

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

