class Users:
    def __init__(self, api, db):
        self.api = api
        self.db = db

    def get_user_info(self, user_id):
        """
        Получает информацию о пользователе
        """
        info = self.api.get_user_info(user_id)[0]
        user = {
            'vk_id': info['id'],
            'age': info['bdate'],
            'city': info['city']['title'] if 'city' in info else None,
            'sex': info['sex'],
            'status': info['relation']
        }
        return user

    def search_users(self, age_from, age_to, city, sex, status):
        """
        Ищет пользователей по заданным параметрам
        """
        users = self.api.search_users(age_from, age_to, city, sex, status)['items']
        return users

    def add_user_to_db(self, user):
        """
        Добавляет информацию о пользователе в базу данных
        """
        self.db.add_user(user)

    def get_user_from_db(self, vk_id):
        """
        Получает информацию о пользователе из базы данных
        """
        return self.db.get_user(vk_id)
