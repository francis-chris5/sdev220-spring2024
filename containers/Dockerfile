FROM python:3

WORKDIR /opt/greeting

COPY ./greet.py .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "greet.py"]