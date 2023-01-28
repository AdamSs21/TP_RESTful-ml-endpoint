#Dockerfile to build a flask app

FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-use-pep517 -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "-m", "flask", "app.py"]