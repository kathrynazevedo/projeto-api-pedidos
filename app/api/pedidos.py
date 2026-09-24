from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.pedido import PedidoCreate, PedidoResponse, PedidoStatusUpdate
from app.services.pedido_service import PedidoService

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def criar_pedido(dados: PedidoCreate, db: Session = Depends(get_db)):
    service = PedidoService(db)
    return service.criar_pedido(dados)

@router.get("", response_model=list[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    service = PedidoService(db)
    return service.listar_pedidos()

@router.get("/{id}", response_model=PedidoResponse)
def consultar_pedido(id: int, db: Session = Depends(get_db)):
    service = PedidoService(db)
    return service.consultar_pedido(id)

@router.patch("/{id}/status", response_model=PedidoResponse)
def alterar_status(id: int, dados: PedidoStatusUpdate, db: Session = Depends(get_db)):
    service = PedidoService(db)
    return service.alterar_status(id, dados.status)