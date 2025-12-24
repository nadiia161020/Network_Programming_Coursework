from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

# Функція аутентифікації (Basic Auth)
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "secret":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return credentials.username

@app.get("/")
def read_root(user: str = Depends(authenticate)):
    return {"message": f"Hello, {user}!", "task": "Coursework Step 1"}