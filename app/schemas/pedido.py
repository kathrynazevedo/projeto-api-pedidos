from datetime import datetime
from pydantic import BaseModel, Field

class PedidoCreate(BaseModel):
    cliente: str = Field(..., min_length=2, max_length=100, description="Nome do cliente")
    produto: str = Field(..., min_length=2, max_length=100, description="Nome do produto")
    quantidade: int = Field(..., gt=0, description="Deve ser maior que zero")
    valor_unitario: float = Field(..., gt=0, description="Valor de uma unidade (maior que zero)")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "cliente": "Márcio",
                    "produto": "Peça Automotiva - Amortecedor",
                    "quantidade": 4,
                    "valor_unitario": 250.50
                }
            ]
        }
    }

class PedidoResponse(BaseModel):
    id: int
    cliente: str
    produto: str
    quantidade: int
    valor_unitario: float
    valor_total: float
    status: str
    data_criacao: datetime

    model_config = {
        "from_attributes": True
    }
class PedidoStatusUpdate(BaseModel):
    status: str = Field(..., min_length=1, max_length=50, description="Novo status do pedido (ex: CONFIRMADO, CANCELADO)")