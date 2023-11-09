import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
import requests

class Parser(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def load_vacancies(self, keyword):
        """Метод для загрузки вакансий с сайта."""
        pass

class HH(Parser):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'only_with_salary': True, 'text': '', 'page': 0, 'per_page': 100}


    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        vacancies = []
        while self.params['page'] != 20:
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            raw_vacancies = response.json()['items']
            vacancies.extend(raw_vacancies)
            self.params['page'] +=1
        return vacancies


class SJ(Parser):
    def __init__(self):
        load_dotenv('.env')
        self._API_KEY = os.getenv('SJ_KEY')
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.headers = {'X-Api-App-Id': self._API_KEY}
        self.params = {'keyword': '', 'count': 100, 'page': 0}


    def load_vacancies(self, keyword):
        self.params['keyword'] = keyword
        vacancies = []
        while self.params['page'] != 5:
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            raw_vacancies = response.json()['objects']
            vacancies.extend(raw_vacancies)
            self.params['page'] +=1
        return vacancies

