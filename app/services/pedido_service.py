from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.pedido_repository import PedidoRepository
from app.schemas.pedido import PedidoCreate
from app.models.pedido import PedidoModel

class PedidoService:
    def __init__(self, db: Session):
        self.repository = PedidoRepository(db)

    def criar_pedido(self, dados: PedidoCreate) -> PedidoModel:
        if dados.quantidade <= 0 or dados.valor_unitario < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Quantidade deve ser maior que zero e valor unitário não pode ser negativo."
            )
        return self.repository.criar(dados)

    def consultar_pedido(self, pedido_id: int) -> PedidoModel:
        pedido = self.repository.consultar_por_id(pedido_id)
        if not pedido:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pedido não encontrado."
            )
        return pedido

    def listar_pedidos(self) -> list[PedidoModel]:
        return self.repository.listar_todos()

    def alterar_status(self, pedido_id: int, novo_status: str) -> PedidoModel:
        pedido = self.repository.atualizar_status(pedido_id, novo_status)
        if not pedido:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pedido não encontrado."
            )
        return pedido