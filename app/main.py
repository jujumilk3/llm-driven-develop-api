import openai
from fastapi import Body, FastAPI, status
from loguru import logger
from pydantic import BaseModel, Field

from app.core.config import configs
from app import utils


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


@app.post("/create-user", status_code=status.HTTP_201_CREATED)
async def create_user(
    nickname: str = Body(..., example="nickname"),
    email: str = Body(..., example="email"),
    password: str = Body(..., example="password"),
):
    return utils.create_user(utils.UserModel(nickname=nickname, email=email, password=password))


@app.post("/create-post", status_code=status.HTTP_201_CREATED)
def create_post(
    user_email: str = Body(..., example="email"),
    title: str = Body(..., example="title"),
    content: str = Body(..., example="content"),
):
    return utils.create_post(user_email=user_email, title=title, content=content)
