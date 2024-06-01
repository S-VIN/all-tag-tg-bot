PROD_ENV = True


if PROD_ENV:
    print("prod env secrets")
    with open("/run/secrets/all_tag_tg_api_id", "r") as file:
        API_ID = file.read()
    with open("/run/secrets/all_tag_tg_token", "r") as file:
        BOT_TOKEN = file.read()
    with open("/run/secrets/all_tag_tg_api_hash", "r") as file:
        API_HASH = file.read()
else:
    print("dev env secrets")
    import secrets
    API_ID = secrets.API_ID
    BOT_TOKEN = secrets.BOT_TOKEN
    API_HASH = secrets.API_HASH