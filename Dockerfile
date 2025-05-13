# 1) Base Python 3.11 slim
FROM python:3.11-slim

# 2) Instala dependencias de sistema
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    # navegador headless
    chromium \
    # driver para Chromium
    chromium-driver \
    # utilidades para descargar y extraer
    wget unzip \
    # libs gráficas / de sistema que Chromium requiere
    fontconfig libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 libdrm2 \
    libgbm1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libnss3 \
    libx11-xcb1 libxcomposite1 libxdamage1 libxext6 libxfixes3 libxrandr2 \
    libxrender1 libxss1 libxtst6 \
 && rm -rf /var/lib/apt/lists/*

# 3) Variables de entorno para Selenium
ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER_PATH=/usr/bin/chromedriver

# 4) Prepara tu aplicación
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copia el código Python
ADD . /app

# 6) Punto de entrada
CMD ["python", "app.py"]
