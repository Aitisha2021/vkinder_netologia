import vk_api
from random import randrange
from vk_api.longpoll import VkLongPoll
from vk_api.exceptions import ApiError

class VKApi:
    def __init__(self, token, token_user):
        self.vk = vk_api.VkApi(token=token)
        self.vk2 = vk_api.VkApi(token=token_user)
        self.api = self.vk2.get_api()
        self.longpoll = VkLongPoll(self.vk)

    def get_user_info(self, user_id):
        """
        Получает информацию о пользователе
        """
        try:
            return self.vk2.users.get(user_id=user_id)
        except ApiError as e:
            print(f"Ошибка VK API: {e}")
            return None

    def search_users(self, age_from, age_to, city, sex, status, count=100, offset=0):
        """
            Ищет пользователей по заданным параметрам
        """
        # Проверка данных
        if not isinstance(age_from, int) or not isinstance(age_to, int) or not isinstance(city, str) or not isinstance(sex, int) or not isinstance(status, int) or not isinstance(count, int) or not isinstance(offset, int):
            raise ValueError("Неверный тип данных аргументов")
        
        try:
            return self.api.users.search(count=count, offset=offset, age_from=age_from, age_to=age_to, city=city, sex=sex, status=status)
        except ApiError as e:
            print(f"Ошибка VK API: {e}")
            return []

    def get_photo_likes(self, owner_id, photo_id):
        """
        Получает количество лайков на фотографии
        """
        try:
            return self.api.likes.getList(type="photo", owner_id=owner_id, item_id=photo_id, filter="likes")
        except ApiError as e:
            print(f"Ошибка VK API: {e}")
            return []

    def get_photo_comments(self, owner_id, photo_id):
        """
        Получает количество комментариев на фотографии
        """
        try:
            return self.api.photos.getComments(owner_id=owner_id, photo_id=photo_id)
        except ApiError as e:
            print(f"Ошибка VK API: {e}")
            return []

    def get_user_photos(self, user_id):
        """
        Получает фотографии пользователя
        """
        try:
            return self.api.photos.get(owner_id=user_id, album_id="profile", extended=1)
        except ApiError as e:
            print(f"Ошибка VK API: {e}")
            return []

    def write_msg(self, user_id, message):
        """
        Отправляет сообщение пользователю с указанным user_id
        """
        try:
            self.vk2.messages.send(user_id=user_id, message=message, random_id=randrange(10 ** 7))
        except ApiError as e:
            print(f"Ошибка VK API: {e}")
