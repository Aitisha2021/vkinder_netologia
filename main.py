from handlers import MessageHandler

def main():
    token = input('Введите ваш VK API токен: ')
    handler = MessageHandler(token)
    handler.run()

if __name__ == "__main__":
    main()