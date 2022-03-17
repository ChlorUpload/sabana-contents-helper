from typing import Optional
from pydantic import BaseModel


class ProcessOptionModel(BaseModel):
    name: str
    start_measure: Optional[int] = None
    end_measure: Optional[int] = None