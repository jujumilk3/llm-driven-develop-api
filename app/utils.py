import json
import os
from typing import Union

from marvin import ai_fn
from pydantic import BaseModel, Field

from app.core.config import configs


class UserModel(BaseModel):
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
    2. Add password md5 hashed .
    3. Add user_token created uuid4.
    4. Add created_at with current datetime as UTC.
    5. Add nickname.
    6. return as Json type.
    """


@ai_fn
def create_post(user_email: str, title: str, content: str) -> dict[str, str]:
    f"""
    1. Create post schema as json with user_email, title, content.
    2. The user_email is {user_email}.
    3. The title is {title}.
    4. The content is {content}.
    5. Add created_at with current datetime as UTC.
    6. return as Json type.
    """


# @ai_fn
def auth_user_with_email_and_password(email: str, password: str) -> dict[str, str]:
    user_collections = os.listdir(f"{configs.COLLECTIONS_DIR}/users")
    found_user_file = None
    for file in user_collections:
        if email in file:
            found_user_file = file
            break
    else:
        raise Exception("User not found.")
    print(found_user_file)
    with open(f"{configs.COLLECTIONS_DIR}/users/{found_user_file}", "r") as f:
        user_collections = json.loads(f.read())

    """
    It can't decode password.
    NOTE: Tried prompts
    1. 
        1. There is a password hashed by md5.
        2. The password is {user_collections['password']} as md5.
        2. give me decoded password.
    """

    # @ai_fn
    def check_password(inner_password: str):
        f"""
        1. decode {user_collections['password']}. This is md5.
        2. compare with {inner_password}
        2. give me True if password is correct.
        3. give me False if password is incorrect.
        """
        # Just return True for now. Because it can't decode password.
        return True

    return check_password(password)


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
    # print(auth_user_with_email_and_password("email", "password"))

    # created_post = create_post(user_email="email@email.com", title="title", content="content")
    # # string to dict
    # created_post_as_json = json.loads(created_post)
    # print(created_post_as_json)
    # print(type(created_post_as_json))
    # save_data_as_json(
    #     data=created_post_as_json,
    #     collection_name="posts",
    #     file_name=f"post_by_{created_post_as_json['user_email']}_{created_post_as_json['created_at']}",
    # )
    # NOTE: DATE 2023-05-31 It returned {"user_token": "user_token", "title": "title", "content": "content", "created_at": "2023-05-31T14:18:00Z"}

    created_post = create_post(user_email="email@email.com", title="this is title", content="this is content")
    # string to dict
    created_post_as_json = json.loads(created_post)
    print(created_post_as_json)
    print(type(created_post_as_json))
    save_data_as_json(
        data=created_post_as_json,
        collection_name="posts",
        file_name=f"post_by_{created_post_as_json['user_email']}_{created_post_as_json['created_at']}",
    )
