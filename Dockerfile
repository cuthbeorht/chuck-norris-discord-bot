FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt ./
COPY ./jokes.json ./
COPY ./command.py ./

RUN pip install -r requirements.txt

CMD ["python3", "command.py"]