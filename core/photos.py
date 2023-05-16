class Photos:
    def __init__(self, api):
        self.api = api

    def get_top_photos(self, user_id, top=3):
        """
        Возвращает топ-3 фотографии пользователя по количеству лайков и комментариев
        """
        photos = self.api.get_user_photos(user_id)
        photo_scores = []

        for photo in photos['items']:
            likes = photo['likes']['count']
            comments = self.api.get_photo_comments(user_id, photo['id'])['count']
            score = likes + comments
            photo_scores.append((photo['id'], score))

        # Сортируем фотографии по оценке и возвращаем топ-3
        photo_scores.sort(key=lambda x: x[1], reverse=True)
        top_photos = photo_scores[:top]

        return [photo_id for photo_id, _ in top_photos]
