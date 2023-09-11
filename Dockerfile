FROM python:3.11-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_DEBUG=False
ENV DJANGO_SECRET_KEY='YOU-SHOULD-SET-THIS-IN-PRODUCTION@#&!$'
ENV DJANGO_ALLOWED_HOSTS='*.onrender.com 127.0.0.1 localhost 0.0.0.0'

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "taskX.wsgi:application"]

