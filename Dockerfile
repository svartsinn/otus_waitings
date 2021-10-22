FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .

RUN mkdir logs
RUN cd logs
RUN touch selenium.log
RUN cd /app
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest"]