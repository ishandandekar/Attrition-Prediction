FROM python:3.9

WORKDIR /serve

COPY ./src ./src
COPY ./config ./config

RUN pip install --upgrade pip && pip install -r serve-requirements.txt --no-cache-dir

CMD [ "python", "./src/api/app.py"]