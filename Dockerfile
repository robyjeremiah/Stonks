FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /Stonks
COPY requirements.txt /Stonks/requirements.txt
RUN pip install -r requirements.txt
COPY . /Stonks

CMD python manage.py runserver 0.0.0.0:8000