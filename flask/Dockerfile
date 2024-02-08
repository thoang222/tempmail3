FROM alpine:3.15.4

WORKDIR /app

RUN apk update && apk add python3 py3-pip git

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]