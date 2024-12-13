from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.Domain.Schemas.Reporte_schema import ReporteRequestModel, ReporteResponseModel, ReporteToUpdateModel

class ReporteRepository(ABC):
    @abstractmethod
    def create(self, reporte: ReporteRequestModel, db: Session) -> ReporteResponseModel:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int, db: Session) -> list[ReporteResponseModel]:
        pass

    @abstractmethod
    def delete(self, id: int, db: Session) -> None:
        pass

    @abstractmethod
    def update(self, id: int, reporte: ReporteToUpdateModel, db: Session) -> ReporteResponseModel:
        pass