from sqlalchemy.orm import Session
from app.models.pedido import PedidoModel
from app.schemas.pedido import PedidoCreate

class PedidoRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, pedido_data: PedidoCreate) -> PedidoModel:
        valor_total = pedido_data.quantidade * pedido_data.valor_unitario
        db_pedido = PedidoModel(
            cliente=pedido_data.cliente,
            produto=pedido_data.produto,
            quantidade=pedido_data.quantidade,
            valor_unitario=pedido_data.valor_unitario,
            valor_total=valor_total,
            status="CRIADO"
        )
        self.db.add(db_pedido)
        self.db.commit()
        self.db.refresh(db_pedido)
        return db_pedido

    def consultar_por_id(self, pedido_id: int) -> PedidoModel | None:
        return self.db.query(PedidoModel).filter(PedidoModel.id == pedido_id).first()

    def listar_todos(self) -> list[PedidoModel]:
        return self.db.query(PedidoModel).all()

    def atualizar_status(self, pedido_id: int, novo_status: str) -> PedidoModel | None:
        pedido = self.consultar_por_id(pedido_id)
        if pedido:
            pedido.status = novo_status
            self.db.commit()
            self.db.refresh(pedido)
        return pedido