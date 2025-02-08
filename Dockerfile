FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install python-dotenv requests

CMD ["python3", "script.py"]
