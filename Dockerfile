FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000         
ENV PORT=10000       

CMD gunicorn app:app --bind 0.0.0.0:$PORT
