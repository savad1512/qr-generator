from pydantic import Field,BaseModel
from typing import Optional,Annotated
from enum import Enum

class CodeType(str, Enum):
    qr = "qr"
    bar_code = "bar code"

class SizeChart(BaseModel):
    width: int = 150
    height: int = 150

class RequestIn(BaseModel):
    chs: Annotated[str, Field(pattern=r'\d{2,4}x\d{2,4}')] = SizeChart
    cht: CodeType
    chl: str