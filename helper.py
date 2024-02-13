from io import BytesIO
import qrcode
from PIL import Image
from schema import SizeChart


async def qr_code_generation(data_url: str, size: str):
    size_chart = await get_size(size)
    qr_code_image = BytesIO()
    obj_qr = qrcode.QRCode(  
        version = 3,  
        error_correction = qrcode.constants.ERROR_CORRECT_L,  
        box_size = 6,
        border = 2
    )
    obj_qr.add_data(data_url)  
    obj_qr.make(fit = True)

    img_obj = obj_qr.make_image(fill_color="black", back_color="white")
    img_obj.save(qr_code_image ,format='PNG')
    qr_code_image.seek(0)


    image = Image.open(qr_code_image)
    image = image.resize((size_chart.width, size_chart.height))
    resized_qr_code = BytesIO()
    image.save(resized_qr_code ,format='PNG')
    
    resized_qr_code.seek(0)
    return resized_qr_code


async def get_size(size: str) -> SizeChart:
    if isinstance(size,str):
        size_chart = SizeChart(
        width=int(size.split("x")[0]),
        height=int(size.split("x")[1])
    )
    else:
        size_chart = SizeChart
    return size_chart