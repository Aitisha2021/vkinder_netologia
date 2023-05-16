class User:
    def __init__(self, vk_id, age, city, sex, status):
        self.vk_id = vk_id
        self.age = age
        self.city = city
        self.sex = sex
        self.status = status

    def to_dict(self):
        """
        Возвращает представление пользователя в виде словаря
        """
        return {
            'vk_id': self.vk_id,
            'age': self.age,
            'city': self.city,
            'sex': self.sex,
            'status': self.status
        }
