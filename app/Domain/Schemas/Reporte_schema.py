from pydantic import BaseModel,ConfigDict
from datetime import datetime

class ReporteRequestModel(BaseModel):
    id: int | None = None
    titulo: str
    paginas: int
    costo: float
    fecha_reporte: datetime
    user_id: int
    
    @classmethod
    def validate_titulo(cls, titulo: str) -> str:
        if len(titulo) < 3:
            raise ValueError('Titulo debe tener mas de 3 caracteres de longitud')
        if len(titulo) > 50:
            raise ValueError('Titulo debe tener menos de 50 caracteres de longitud')
        return titulo

    model_config = ConfigDict(json_schema_extra={
        'example': {
            'titulo': 'Reporte de ventas',
            'paginas': 10,
            'costo': 100.00,
            'fecha_reporte': '2023-01-01T00:00:00',
            'user_id': 1
        }
    })
    
class ReporteResponseModel(BaseModel):
    id: int
    titulo: str
    paginas: int
    costo: float
    fecha_reporte: datetime
    user_id: int
    
    model_config = ConfigDict(from_attributes=True)

class ReporteToUpdateModel(BaseModel):
    titulo: str | None = None
    paginas: int | None = None
    costo: float | None = None
    fecha_reporte: datetime | None = None

    model_config = ConfigDict(json_schema_extra={
        'example': {
            'titulo': None,
            'paginas': None,
            'costo': None,
            'fecha_reporte': None
        }
    })