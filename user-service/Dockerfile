# Python 3.9 slim imajı ile başla
FROM python:3.9-slim

# Çalışma dizini oluştur
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Flask uygulamasını çalıştır
CMD ["python", "app.py"]
