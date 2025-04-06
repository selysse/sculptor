FROM python:3.11-slim

RUN mkdir /sculptor
WORKDIR /sculptor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src /sculptor/src

CMD ["python", "./src/main.py"]