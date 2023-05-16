import vk_api
from random import randrange
from vk_api.longpoll import VkLongPoll

class VKApi:
    def __init__(self, token):
        self.vk_session = vk_api.VkApi(token=token)
        self.vk = self.vk_session.get_api()
        self.longpoll = VkLongPoll(self.vk_session)

    def get_user_info(self, user_id):
        """
        Получает информацию о пользователе
        """
        return self.vk.users.get(user_id=user_id)

    def search_users(self, age_from, age_to, city, sex, status):
        """
        Ищет пользователей по заданным параметрам
        """
        return self.vk.users.search(count=1000, age_from=age_from, age_to=age_to, city=city, sex=sex, status=status)

    def get_photo_likes(self, owner_id, photo_id):
        """
        Получает количество лайков на фотографии
        """
        return self.vk.likes.getList(type="photo", owner_id=owner_id, item_id=photo_id, filter="likes")

    def get_photo_comments(self, owner_id, photo_id):
        """
        Получает количество комментариев на фотографии
        """
        return self.vk.photos.getComments(owner_id=owner_id, photo_id=photo_id)

    def get_user_photos(self, user_id):
        """
        Получает фотографии пользователя
        """
        return self.vk.photos.get(owner_id=user_id, album_id="profile", extended=1)
    
    def write_msg(self, user_id, message):
        """
        Отправляет сообщение пользователю с указанным user_id
        """
        self.vk.messages.send(user_id=user_id, message=message, random_id=randrange(10 ** 7))