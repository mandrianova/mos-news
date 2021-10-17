FROM python:3.7
WORKDIR /app
ADD requirements.txt /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /app
