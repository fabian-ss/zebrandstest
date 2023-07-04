FROM python:3.10.4-alpine3.15

WORKDIR /app

RUN apk update \ && apk add gcc musl-dev postgresql-dev python3-dev libffi-dev \ && pip3 install

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]

# RUN pip install --upgrade pip
# RUN pip install gunicorn
# ADD ./app/requirements.txt /app/
# RUN pip install -r requirements.txt

# ADD ./app /app 

# RUN chmod +x /app/server-entrypoint.sh
# RUN chmod +x /app/worker-entrypoint.sh
# FROM python:3.

# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# # RUN apk add --update --no-cache --virtual .build-deps \
# #     ca-certificates gcc postgresql-dev python3-dev linux-headers musl-dev \
# #     libffi-dev jpeg-dev zlib-dev g++ 

# COPY . /app


# EXPOSE 8000

# CMD ["sh","./django.sh"]