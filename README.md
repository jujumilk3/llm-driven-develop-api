# llm-driven-development-api

Repository for Concept Research of LDD(LMM Driven Development)

## Description

Code Repository for Researching the Concept of "Future Programming" Discussed in Paul Graham's Book, "Hackers and Painters"

## Commands

1. Install python packages

    ``` shell
    % pip install -r requirements.txt
    # or
    % poetry install
    ```
    ※ marvin is a huge package, so it takes a long time to install.

2. Setup marvin with openai api key

    ``` shell
    % marvin setup-openai
    # And type your openai api key
    ```

    -> You can check if it has been properly configured by running `app/utils.py` file.

3. Run api

    ```shell
    % uvicorn app.main:app --reload
    ```

## Packages

1. <https://platform.openai.com/docs/api-reference/authentication?lang=python>
2. <https://github.com/PrefectHQ/marvin>
3. <https://github.com/chroma-core/chroma>

## References

1. <https://en.wikipedia.org/wiki/Hackers_%26_Painters>
