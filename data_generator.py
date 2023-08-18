import csv
from faker import Faker
from russian_names import RussianNames


fake = Faker("ru")
HEADER = (
    "Фамилия",
    "Имя",
    "Отчество",
    "Организация",
    "Раб. телефон",
    "Лич. телефон",
)

def gen_data() -> None:
    """
    Generate data for csv file.
    """
    with open("phone_book.csv", "w", encoding="utf8", newline="") as f:

        writer = csv.writer(f)
        writer.writerow(HEADER)
        for _ in range(100):
            fname_patron_sname = RussianNames().get_person().split()
            row = [fname_patron_sname[-1]] + fname_patron_sname[:-1]
            row.extend(
                [fake.company(), "7" + fake.msisdn()[:10], "+7" + fake.msisdn()[:10]]
            )
            writer.writerow(row)


if __name__ == "__main__":
    gen_data()
