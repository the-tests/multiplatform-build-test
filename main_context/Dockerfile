ARG BASE_IMAGE
FROM ${BASE_IMAGE}

RUN pip install Flask

ARG APP_PORT=1234
ENV APP_PORT=${APP_PORT}
EXPOSE ${APP_PORT}

WORKDIR /app

COPY hello.py ./
COPY --from=assets favicon.ico ./

ENTRYPOINT [ "python", "/app/hello.py" ]
