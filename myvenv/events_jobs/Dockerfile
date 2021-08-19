FROM python:3.8-slim-buster

RUN mkdir /eventjobs
COPY requirements.txt /eventjobs
WORKDIR /eventjobs
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]