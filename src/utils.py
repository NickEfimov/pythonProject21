from vacancy import Vacancy


def get_hh_vacancies(hh_vacancies):
    vacancies = []
    for vacancy in hh_vacancies:
        if vacancy.get('salary').get('from'):
            vacancies.append(
                Vacancy(
                    title=vacancy.get('name'),
                    description=vacancy.get('snippet').get('requirement'),
                    salary=vacancy.get('salary').get('from'),
                    currency=vacancy.get('salary').get('currency')
                )
            )

    return vacancies


def get_sj_vacancies(sj_vacancies):
    vacancies = []
    for vacancy in sj_vacancies:
        if vacancy.get('payment_from'):
            vacancies.append(
                Vacancy(
                    title=vacancy.get('profession'),
                    description=vacancy.get('candidate'),
                    salary=vacancy.get('payment_from'),
                    currency=vacancy.get('currency')
                )
            )

    return vacancies


def to_dict(raw_vacancies):
    vacancies = []
    for vacancy in raw_vacancies:
        vacancies.append(
            {
                'title': vacancy.title,
                'description': vacancy.candidate,
                'salary': vacancy.payment_from,
                'currency': vacancy.currency
            }
        )
    return vacancies