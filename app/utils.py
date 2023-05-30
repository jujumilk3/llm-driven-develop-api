from marvin import ai_fn
from pydantic import BaseModel, Field


class UserModel(BaseModel):
    user_token: str = Field(..., example="user_token")
    nickname: str = Field(..., example="nickname")
    email: str = Field(..., example="email")
    password: str = Field(..., example="password")


@ai_fn
def list_fruits(n: int) -> list[str]:
    f"""Generate a list of {n} fruits."""


@ai_fn
def create_user(user_model: UserModel) -> dict[str, str]:
    f"""
    1. The data is {user_model.dict()}
    2. Change Password with md5.
    3. Json type.
    """


if __name__ == "__main__":
    # print(list_fruits(3))
    # NOTE: Date 2023-05-30 It returned ['apple', 'banana', 'orange']
    user_model = UserModel(
        user_token="user_token",
        nickname="nickname",
        email="email@email.com",
        password="password",
    )
    created_user = create_user(user_model)
    print(created_user)
    # NOTE: DATE 2023-05-30 It returned {'user_token': 'user_token', 'nickname': 'nickname', 'email': 'email@email.com', 'password': '5f4dcc3b5aa765d61d8327deb882cf99'}
