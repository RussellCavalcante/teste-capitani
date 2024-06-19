FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY wait-for-it.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-it.sh

CMD ["sh", "-c", "wait-for-it.sh kafka:9092 -- wait-for-it.sh db:5432 -- uvicorn app.main:app --host 0.0.0.0 --port 8000"]
