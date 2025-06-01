FROM python:3.9-slim

# Tambahkan git, ffmpeg, dan dependensi dasar
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone repo ke direktori yang diinginkan
RUN git clone -b Kazu-Userbot https://github.com/rmjstore/Kazu-Userbot /home/Kazuuserbot/ \
    && chmod 777 /home/Kazuuserbot \
    && mkdir -p /home/Kazuuserbot/bin/

# Salin config
COPY ./sample_config.env ./config.env* /home/Kazuuserbot/

WORKDIR /home/Kazuuserbot/

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install av --no-binary av
RUN pip install -r requirements.txt

# Jalankan aplikasi
CMD ["bash", "start"]
