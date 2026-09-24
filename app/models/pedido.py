import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String
from app.database import Base

class PedidoModel(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cliente = Column(String, nullable=False)
    produto = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Float, nullable=False)
    valor_total = Column(Float, nullable=False)
    status = Column(String, default="CRIADO", nullable=False)
    data_criacao = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)