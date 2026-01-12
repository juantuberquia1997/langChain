from pydantic import BaseModel, Field

class CV_analyzer(BaseModel):
  name: str = Field(description="Nombre del candidato a la vacante")
  time_experience: int = Field(description="Años de experiencia del candidato")
  strengths: list[str] = Field(description="Listado de fortalezas del candidato, 3-4 fortalezas")
  education: str = Field(description="Nivel educativo mas alto del candidato")
  experience_relevant: str = Field(description="Resumen corto de la experiencia mas relevante")
  weaknesses: list[str]= Field(description="Listado de debilidades del candidado, 3-4 debilidades")
  toImprove: list[str]= Field(description="Listado de oportunidades de mejora del candidado, 3-4 oportunidades de mejora")
  percentaje: int = Field(description="Porcentaje de ajuste del puesto (0-100) en la vacante", ge=0, le=100)