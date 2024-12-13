from app.Infrastructure.Database import Base
from datetime import datetime,timezone
from sqlalchemy import DateTime, Integer, String,ForeignKey,FLOAT
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.Domain.Model.user import User

class Reporte(Base):
    __tablename__ = 'reporte'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(50))
    paginas: Mapped[int] = mapped_column(Integer)
    costo: Mapped[float] = mapped_column(FLOAT)
    fecha_reporte: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'),index=True)
    ##user: Mapped[User] = relationship("User", back_populates="reportes")
    def model_dump(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'paginas': self.paginas,
            'costo': self.costo,
            'fecha_reporte': self.fecha_reporte.__str__(),
            'user_id': self.user_id
        }
