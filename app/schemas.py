from pydantic import BaseModel, EmailStr
from typing import List, Optional

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int

    class Config:
        from_attributes = True  

class CompanyBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int
    obrigacoes: List[ObrigacaoAcessoria] = []

    class Config:
        from_attributes = True 