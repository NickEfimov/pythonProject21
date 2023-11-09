from base_api import HH, SJ
from utils import get_hh_vacancies, get_sj_vacancies

hh = HH()
sj = SJ()
hh_vacancies = hh.load_vacancies('python')
sj_vacancies = sj.load_vacancies('python')
hh_vacancies = get_hh_vacancies(hh_vacancies)
sj_vacancies = get_sj_vacancies(sj_vacancies)
vacancies = hh_vacancies + sj_vacancies
print(vacancies[:3])
vacancies = sorted(vacancies, reverse=True)
print(vacancies[:3])
vacancies = sorted(vacancies, reverse=False)
print(vacancies[:3])