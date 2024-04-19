# Utilisez une image de Python officielle en tant qu'image de base
FROM python:3.11-alpine

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le contenu de votre projet FastAPI dans le répertoire de travail du conteneur
COPY . .

# Installez les dépendances Python
RUN pip install fastapi uvicorn beautifulsoup4 requests

# Exposez le port sur lequel votre application FastAPI fonctionne
EXPOSE 8000

# Commande pour démarrer votre application FastAPI
CMD ["uvicorn", "chat_api:app", "--host", "0.0.0.0", "--port", "8000"]
