from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.ObrigacaoAcessoria)
def create_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@router.get("/", response_model=List[schemas.ObrigacaoAcessoria])
def list_obrigacoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    obrigacoes = db.query(models.ObrigacaoAcessoria).offset(skip).limit(limit).all()
    return obrigacoes

@router.get("/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def get_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return obrigacao

@router.put("/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def update_obrigacao(obrigacao_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    
    for key, value in obrigacao.dict().items():
        setattr(db_obrigacao, key, value)
    
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@router.delete("/{obrigacao_id}")
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    
    db.delete(obrigacao)
    db.commit()
    return {"message": "Obrigação excluída com sucesso"}