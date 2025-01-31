FROM python:3.9-slim
WORKDIR /app

# Installer les dépendances
RUN pip install flask pymongo

# Copier les fichiers
COPY . .

# Démarrer l'application Flask
CMD ["python", "app.py"]
