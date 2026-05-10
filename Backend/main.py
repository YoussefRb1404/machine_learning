import os
import sys

# Ajouter le dossier Backend au chemin de recherche pour permettre les imports relatifs en déploiement
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.classification_routes import router as prediction_router

app = FastAPI(title="ML Backend API")

# Configuration CORS pour permettre au frontend de communiquer avec le backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, remplacez par l'URL de votre frontend (ex: ["https://votre-app.streamlit.app"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prediction_router, prefix="/api", tags=["Prediction"])

@app.get("/")
def home():
    return {"message": "Backend opérationnel 🚀"}