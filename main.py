from handlers import MessageHandler
from config import *


def main():
    token = TOKEN_GROUP
    token_user = TOKEN_USER
    handler = MessageHandler(token, token_user)
    handler.run()

if __name__ == "__main__":
    main()