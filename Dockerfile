FROM python:latest

LABEL Maintainer="stepan"

COPY requirements.txt /home/
WORKDIR /home

COPY main.py ./
COPY config.py ./
RUN pip install -r /home/requirements.txt

CMD [ "python", "./main.py"]