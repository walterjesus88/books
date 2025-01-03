FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y lo instala
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . /app/

# Ejecuta collectstatic para recopilar los archivos estáticos
RUN python manage.py collectstatic --noinput

# Expone el puerto que usará el servidor
EXPOSE 8000

# Comando para ejecutar Gunicorn (servidor de producción)
CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]

