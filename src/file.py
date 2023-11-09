import json
from abc import ABC, abstractmethod

class File(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def load_vacancies(self, vacancies):
        """Метод для загрузки вакансий с сайта."""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Метод для загрузки вакансий с сайта."""
        pass

class JSONSaver(File):
    def load_vacancies(self, vacancies):
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(vacancies, ensure_ascii=False))