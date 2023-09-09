FROM python:3.11.0a1-alpine3.14

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_DEBUG=False
ENV DJANGO_SECRET_KEY='YOU-SHOULD-SET-THIS-IN-PRODUCTION@#&!$'
ENV DJANGO_ALLOWED_HOSTS='*.render.com 127.0.0.1 localhost 0.0.0.0'

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN --mount=type=cache,target=/var/cache/apk \
    --mount=type=cache,target=/var/lib/apk \
    apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "hngx.wsgi:application"]

