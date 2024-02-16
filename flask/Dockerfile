FROM thobaby/temp_mail:v1

WORKDIR .
RUN apk update && apk add python3 py3-pip git
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

ENV PORT=5000
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app:app"]