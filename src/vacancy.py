class Vacancy:
    def __init__(self, title, description, currency, salary):
        self.title = title
        self.description = description
        self.currency = currency
        self.salary = salary


    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title}, salary={self.salary}, currency={self.currency})'

    def __str__(self):
        return self.title

    def __lt__(self, other):
        return self.salary < other.salary
