from fastapi import Header, HTTPException
from app.core.config import API_KEY

def verify_api_key(
    x_api_key: str = Header(None),
    authorization: str = Header(None)
):
    # GUVI tester uses x-api-key
    if x_api_key:
        if x_api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return

    # fallback (your original Bearer support)
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        if token == API_KEY:
            return

    raise HTTPException(status_code=401, detail="Unauthorized")
