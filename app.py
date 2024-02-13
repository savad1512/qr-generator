
from typing import Annotated

from fastapi import FastAPI,Query
from fastapi.responses import Response,StreamingResponse
from mangum import Mangum

from schema import CodeType
from utils.helper import qr_code_generation
 
app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "1"}

@app.get("/generate-qr")
async def root(
    cht: CodeType,
    chl: str,
    chs: Annotated[str, Query(..., regex=r'\d{2,4}x\d{2,4}')] = '150x150'
):
    if cht == CodeType.qr:       
        image_ = await qr_code_generation(chl,chs)
        return StreamingResponse(image_, media_type="image/png")        
    else:
         return Response(status_code=400, content="Invalid cht")
    
handler = Mangum(app)