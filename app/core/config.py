import os
from pathlib import Path


class BaseConfigs:
    APP_ROOT_DIR: str = Path(__file__).parent.parent.parent
    APP_NAME: str = "LDD API"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_ORG_KEy: str = os.getenv("OPENAI_ORG_KEY")


configs = BaseConfigs()
