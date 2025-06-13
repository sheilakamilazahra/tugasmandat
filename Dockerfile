# Gunakan image Python resmi sebagai base image
FROM python:3.9-slim-buster

# Atur direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke direktori kerja
COPY requirements.txt .

# Instal dependensi Python
RUN pip install -r requirements.txt

# Salin seluruh isi direktori saat ini (termasuk app.py) ke direktori kerja di container
COPY . .

# Ekspos port 5000 karena aplikasi Flask akan berjalan di port ini
EXPOSE 5000

# Perintah untuk menjalankan aplikasi ketika container dimulai
CMD ["python", "app.py"]