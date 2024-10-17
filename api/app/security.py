from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.settings import settings
import secrets

security = HTTPBasic()

def authenticate_user(credentials: HTTPBasicCredentials = Security(security)):
    correct_username = secrets.compare_digest(credentials.username, settings.USERNAME)
    correct_password = secrets.compare_digest(credentials.password, settings.PASSWORD)
    
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
