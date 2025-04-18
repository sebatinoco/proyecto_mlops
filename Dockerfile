FROM python:3.12-slim

# Evita que Python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Evita el almacenamiento en caché de pip
ENV PIP_NO_CACHE_DIR=1

# Establece el directorio de trabajo
WORKDIR /app

# Copia solo los archivos necesarios para instalar las dependencias
COPY requirements.txt .

# Instala dependencias en un paso separado para aprovechar el cache
RUN pip install --upgrade pip && pip install -r requirements.txt

# Luego copia el resto de la aplicación
COPY . .

# Expone el puerto
EXPOSE 8000

# Usa CMD para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
