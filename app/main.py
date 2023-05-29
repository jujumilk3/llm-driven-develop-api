from fastapi import FastAPI, status
from app.core.config import configs


app = FastAPI(
    title=configs.APP_NAME,
)


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {"status": "ok"}
