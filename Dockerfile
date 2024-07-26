FROM python:3.12.4-alpine3.20

ARG BOT_TOKEN
ENV BOT_TOKEN=${BOT_TOKEN}

WORKDIR app
COPY . .

RUN apk update
RUN pip install -r requirements.txt
RUN pip install python-telegram-bot --upgrade

CMD ["python", "app.py"]