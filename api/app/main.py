from fastapi import FastAPI, Depends

from app.security import authenticate_user
from app.routers import public, pdf
from app.settings import settings


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    contact={
        "name": "Guigoz Herve",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
    openapi_tags=[
        {
            "name": "Schema",
            "description": "Retrieve the schema of the PDF form",
        },
        {
            "name": "Preview",
            "description": "Get a preview of the PDF form",
        },
        {
            "name": "Fill",
            "description": "Fill the PDF form with the given data (key:value,other:value).",
        },
    ],
)

app.include_router(
    public.router,
    prefix="/api/ping"
)
app.include_router(
    pdf.router,
    prefix="/api/pdf",
    dependencies=[Depends(authenticate_user)]
)

# --------------------------------------------------------------------------------
# Middlewares
# --------------------------------------------------------------------------------
@app.middleware("http")
async def cors_middlewares(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response
