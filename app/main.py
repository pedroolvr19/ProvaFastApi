from fastapi import FastAPI
from app.api.endpoints import companies, obligations
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gerenciamento de Obrigações Acessórias",
    description="API para gerenciar empresas e suas obrigações acessórias",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Bem-vindo à API de Gerenciamento de Obrigações Acessórias",
        "documentacao": "/docs",
        "endpoints": {
            "empresas": "/empresas",
            "obrigacoes": "/obrigacoes"
        }
    }

app.include_router(
    companies.router,
    prefix="/empresas",
    tags=["empresas"]
)

app.include_router(
    obligations.router,
    prefix="/obrigacoes",
    tags=["obrigacoes"]
)