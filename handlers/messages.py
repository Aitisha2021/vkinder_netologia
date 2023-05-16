from vk_api.longpoll import VkEventType
from core import VKApi, Users, Photos, Database

class MessageHandler:
    def __init__(self, token):
        self.api = VKApi(token)
        self.users = Users(self.api, Database())
        self.photos = Photos(self.api)

    def handle(self, event):
        """
        Обрабатывает входящее сообщение
        """
        request = event.text

        if request == "привет":
            self.api.write_msg(event.user_id, f"Привет, {event.user_id}")
        elif request == "пока":
            self.api.write_msg(event.user_id, "Пока((")
        elif request.startswith('find'):
            params = request.split()[1:]  # разбиваем сообщение на части
            age_from, age_to, city, sex, status = params
            users = self.users.search_users(age_from, age_to, city, sex, status)
            for user in users:
                top_photos = self.photos.get_top_photos(user['id'])
                self.api.write_msg(event.user_id, f"Найден пользователь {user['id']}. Топ фотографии: {top_photos}")
        else:
            self.api.write_msg(event.user_id, "Не понял вашего запроса...")

    def run(self):
        """
        Запускает обработчик сообщений
        """
        for event in self.api.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.handle(event)
