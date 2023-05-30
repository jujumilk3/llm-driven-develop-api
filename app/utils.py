import json
import os
from typing import Union

from marvin import ai_fn
from pydantic import BaseModel, Field

from app.core.config import configs


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


# @ai_fn
def auth_user_with_email_and_password(email: str, password: str) -> dict[str, str]:
    user_collections = os.listdir(f"{configs.COLLECTIONS_DIR}/users")
    found_user_file = None
    for file in user_collections:
        if email in file:
            found_user_file = file
            break
    print(found_user_file)
    return user_collections
    # f"""
    # 1. The data is {user_model.dict()}
    # 2. Change Password with md5.
    # 3. Json type.
    # """


def save_data_as_json(data: Union[dict, list], collection_name: str, file_name: str):
    # create dir if not exists
    target_dir: str = f"{configs.COLLECTIONS_DIR}/{collection_name}/"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    with open(f"{target_dir}/{file_name}.json", "w") as f:
        f.write(json.dumps(data))


if __name__ == "__main__":
    pass
    # print(list_fruits(3))
    # NOTE: Date 2023-05-30 It returned ['apple', 'banana', 'orange']
    # user_model = UserModel(
    #     user_token="user_token",
    #     nickname="nickname",
    #     email="email@email.com",
    #     password="password",
    # )
    # created_user = create_user(user_model)
    # print(created_user)
    # save_data_as_json(
    #     data=created_user,
    #     collection_name="users",
    #     file_name=f"user_{created_user['email']}",
    # )
    # NOTE: DATE 2023-05-30 It returned {'user_token': 'user_token', 'nickname': 'nickname', 'email': 'email@email.com', 'password': '5f4dcc3b5aa765d61d8327deb882cf99'}
    print(auth_user_with_email_and_password("email", "password"))
