FROM python:3.8-slim-bookworm

ADD . ./app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4001

CMD ["python","./app.py"]
