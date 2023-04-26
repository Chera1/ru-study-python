class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if input_list:
            max_element = sorted(input_list)[-1]
            return list(map(lambda x: max_element if x > 0 else x, input_list))
        else:
            return []

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if query not in input_list:
            return -1
        low = 0
        high = len(input_list)
        return ListExercise.binary_search(input_list, low, high, query)

    @staticmethod
    def binary_search(input_list: list[int], low, high, query):
        """
        Реализация функции бинарного поиска требуемого индекса по переданному списку
        :param input_list: Исходный список
        :param low: Нижнее значение
        :param high: Верхнее значение
        :param query Искомый элемент
        :return: Искомый номер элемента
        """
        mid = (low + high) // 2
        if input_list[mid] != query:
            if query < input_list[mid]:
                return ListExercise.binary_search(input_list, low, mid - 1, query)
            return ListExercise.binary_search(input_list, mid + 1, high, query)
        else:
            return mid