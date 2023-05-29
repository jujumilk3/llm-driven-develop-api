from marvin import ai_fn


@ai_fn
def list_fruits(n: int) -> list[str]:
    f"""Generate a list of {n} fruits."""


if __name__ == "__main__":
    print(list_fruits(3))
    # NOTE: Date 2023-05-30 It returned ['apple', 'banana', 'orange'].
