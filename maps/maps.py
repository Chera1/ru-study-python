from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        list_of_rating = list(filter(lambda x: x != 0, map(MapExercise.calculate_rating, list_of_movies)))
        average = sum(list_of_rating) / len(list_of_rating)
        return average

    @staticmethod
    def calculate_rating(movie: dict) -> float:
        if ',' in movie['country'] and ['rating_kinopoisk'] and float(movie['rating_kinopoisk']) > 0:
            return float(movie['rating_kinopoisk'])
        return 0.0

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        count = map(MapExercise.calculate_chars,
                    filter(lambda x: x['rating_kinopoisk'] and float(x['rating_kinopoisk']) >= rating, list_of_movies))
        return sum(count)

    @staticmethod
    def calculate_chars(movie: dict) -> int:
        return movie['name'].count('и')
