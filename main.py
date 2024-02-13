
from typing import Annotated
import io
import os

from mangum import Mangum

from fastapi import FastAPI,Query
from fastapi.responses import Response,StreamingResponse

from schema import CodeType
from utils.helper import qr_code_generation
from PIL import Image
 
app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "1"}

@app.get("/generate-qr")
async def get_qr(
    cht: CodeType,
    chl: str,
    chs: Annotated[str, Query(..., regex=r'\d{2,4}x\d{2,4}')] = '150x150'
):
    if cht == CodeType.qr:
        file_name = await qr_code_generation(chl,chs)
        return StreamingResponse(file_name, media_type="image/png")
    else:
         return Response(status_code=400, content="Invalid cht")
    
handler = Mangum(app)