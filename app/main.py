import openai
from fastapi import FastAPI, status
from loguru import logger
from pydantic import BaseModel, Field

from app.core.config import configs


def create_app():
    # init app
    _app = FastAPI(
        title=configs.APP_NAME,
    )

    try:
        # init openai api
        openai.api_key = configs.OPENAI_API_KEY
        openai.organization = configs.OPENAI_ORG_KEY
        # it returns error if api key or org is invalid
        openai.Engine.list()
    except Exception as e:
        logger.error(f"OpenAI API init failed: {e}")
        raise e

    return _app


app = create_app()


class HealthCheckResponse(BaseModel):
    status: str = Field(..., example="ok")


@app.get("/healthcheck", status_code=status.HTTP_200_OK, response_model=HealthCheckResponse)
def healthcheck():
    return {"status": "ok"}
