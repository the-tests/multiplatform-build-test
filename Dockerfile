FROM python:3.12.3-alpine

RUN pip install Flask

ENV APP_PORT=8080
EXPOSE 8080

WORKDIR /app

COPY hello.py favicon.ico ./

ENTRYPOINT [ "python", "/app/hello.py" ]
