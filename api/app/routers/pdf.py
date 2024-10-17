from typing import Annotated, Any, Dict
from PyPDFForm import PdfWrapper
from fastapi import APIRouter, Depends, File, Form, Response, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

router = APIRouter()

# --------------------------------------------------------------------------------
# Schemas
# --------------------------------------------------------------------------------
class Schema(BaseModel):
    type: str
    properties: Dict[str, Any]

# --------------------------------------------------------------------------------
# Services
# --------------------------------------------------------------------------------
class Pdf:
    def __init__(self, upload: UploadFile):
        self.pdf = PdfWrapper(upload.file)

    def schema(self) -> Schema:
        return self.pdf.schema

    def preview(self) -> bytes:
        return self.pdf.preview

    def fill(self, data: Dict[str, any]) -> bytes:
        filled = self.pdf.fill(data)
        return filled.read()

# --------------------------------------------------------------------------------
# Dependencies
# --------------------------------------------------------------------------------
def pdf(file: UploadFile):
    return Pdf(file)


# --------------------------------------------------------------------------------
# Controllers
# --------------------------------------------------------------------------------
@router.post("/schema", response_model=Schema, tags=["Schema"])
def schema(
    file: Pdf = Depends(pdf)
) -> Schema:
    try:
        return file.schema()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting PDF schema: {str(e)}")

@router.post("/fill", response_class=FileResponse, tags=["Fill"])
async def fill(
    file: Annotated[UploadFile, File()],
    data: Annotated[str, Form()],
):
    try:
        pdf = Pdf(file)
        # Split data by comma and convert to dictionary
        data_dict = dict(item.split(':') for item in data.split(','))
        filled_pdf = pdf.fill(data_dict)

        return Response(content=filled_pdf, media_type="application/pdf", headers={"Content-Disposition": f"attachment; filename=filled_form.pdf"})
    except Exception as e:
        return Response(content=f"Error filling PDF: {str(e)}", status_code=500)
