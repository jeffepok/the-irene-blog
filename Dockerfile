FROM python:3.8.11-alpine3.14

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk add --update --no-cache g++ libxslt-dev

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]
