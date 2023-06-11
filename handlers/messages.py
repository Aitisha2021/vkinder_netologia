from vk_api.longpoll import VkEventType
from core import VKApi, Users, Photos, Database

class MessageHandler:
    def __init__(self, token, token_user):
        self.api = VKApi(token, token_user)
        self.user_token = token_user
        self.users = Users(self.api, Database())
        self.photos = Photos(self.api)

        self.search_params = {
            'age_from': None,
            'age_to': None,
            'city': None,
            'sex': None,
            'status': None
        }

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
            if len(params) < 5:
                self.api.write_msg(event.user_id, "Недостаточно параметров для поиска. Введите параметры в следующем формате:\n"
                                                 "find [age_from] [age_to] [city] [sex] [status]")
                return

            self.search_params['age_from'], self.search_params['age_to'], self.search_params['city'], \
                self.search_params['sex'], self.search_params['status'] = params

            # Код для отправки пользователю с сохранением и поэтапным выводом анкет пользователей
            offset = 0
            users = self.search_users(**self.search_params, count=50, offset=offset)
            user_list = []

            while users:
                user_list.extend(users)
                offset += 50
                users = self.search_users(**self.search_params, count=50, offset=offset)

            for user in user_list:
                top_photos = self.photos.get_top_photos(user['id'])
                self.api.write_msg(event.user_id, f"Найден пользователь {user['id']}. Топ фотографии: {top_photos}")

        elif request.startswith('set'):
            params = request.split()[1:]  # разбиваем сообщение на части
            if len(params) != 2:
                self.api.write_msg(event.user_id, "Некорректный формат команды. Введите команду в следующем формате:\n"
                                                 "set [параметр] [значение]")
                return

            param, value = params
            if param not in self.search_params:
                self.api.write_msg(event.user_id, f"Некорректный параметр: {param}. Доступные параметры: {', '.join(self.search_params.keys())}")
                return

            self.search_params[param] = value
            self.api.write_msg(event.user_id, f"Параметр {param} установлен на значение {value}")
        elif request == 'show':
            self.api.write_msg(event.user_id, f"Текущие параметры поиска:\n{self.search_params}")
        else:
            self.api.write_msg(event.user_id, "Не понял вашего запроса...")

    def run(self):
        """
        Запускает обработчик сообщений
        """
        for event in self.api.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.handle(event)
