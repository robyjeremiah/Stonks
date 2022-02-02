FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /Stonks
WORKDIR /Stonks
ADD requirements.txt /Stonks/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /Stonks/
