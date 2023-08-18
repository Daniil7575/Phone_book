import csv
from typing import Dict, List, Tuple, Union
import shutil
import os

# CSV header
HEADER = (
    "Фамилия",
    "Имя",
    "Отчество",
    "Организация",
    "Раб. телефон",
    "Лич. телефон",
)


class PhoneBook:
    """
    A class representing a book of phone numbers.

    Parametrs
    -----
    book_csv_path: str
        A path to a source csv file.
    header: Union[Tuple[str], List[str]]
        A csv header of source file.
    page_size: int
        Number of rows per page.
    """
    def __init__(
        self,
        book_csv_path: str,
        header: Union[Tuple[str], List[str]] = HEADER,
        page_size: int = 10,
    ) -> None:
        self.path: str = book_csv_path
        self.page_size: int = page_size
        self.header = header
        self.path_tmp = "tmp.csv"

    def _get_page(self, page: int) -> List[List[str]]:
        """
        Get page with rows.

        :param page: Page number in the book.
        :returns: List of rows, represented by lists of values.
        """
        rows = []
        with open(self.path, "r", encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            # Skip header.
            next(reader)
            try:
                # Skip to page.
                [next(reader) for _ in range((page - 1) * self.page_size)]
                cntr = 0
                while cntr < self.page_size:
                    rows.append(next(reader))
                    cntr += 1
            except StopIteration:
                # "pass" because there is no handling needed, just return a value
                pass
        return rows

    def print_page(self, page: int) -> None:
        """
        Display page in console.

        :param page: Page number in the book. Starts with 1.
        """
        rows = self._get_page(page)
        if not rows:
            print("В книге нет такой страницы.")
        print(*[" ".join(row) for row in rows], sep="\n")

    def add_new_row(self, data: Union[Tuple[str], List[str]]) -> None:
        """
        Add new row to a file.

        :param data: A list(tuple) with data for new record. Contains only values.
        """
        # Very simple validation
        if len(data) != len(self.header):
            raise TypeError(
                "Incorrect input row data. "
                "Please make sure that the input data matches the csv header. "
                f"\nCSV HEADER: {self.header}"
            )
        with open(self.path, "a", encoding="utf8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
            print(f"Запись успешно создана!")

    def _deltmp(self):
        """
        Delete tmp file, which is created for the duration of the row update.
        """
        os.remove(self.path_tmp)

    def edit_row(self, personal_phone: str, changes: Dict[str, str] = None):
        """
        Edit row: apply given changes to a row with personal_number.

        Better do copy of source file before using.

        :param personal_phone: The personal phone number that will be used
        to search for the record that needs to be changed.
        :param changes: A dict with column name as a key and new values as a value.
        """
        try:
            with open("tmp.csv", "w", newline="", encoding="utf8") as tmpfile:
                with open(self.path, "r", newline="", encoding="utf8") as csvfile:
                    reader = csv.DictReader(csvfile, fieldnames=self.header)
                    writer = csv.DictWriter(tmpfile, fieldnames=self.header)
                    for row in reader:
                        if row["Лич. телефон"] == personal_phone:
                            for key, val in changes.items():
                                row[key] = val
                        writer.writerow(row)
            shutil.move(self.path_tmp, self.path)
        except Exception as e:
            print(e)
            # Delete tmp file if exception occured
            self._deltmp()

    def find(self, filter: Dict[str, str]) -> None:
        """
        Find rows by given filters and print them to console.

        :param filter: A dict with column name as a key and search param as a value.
        """
        with open(self.path, "r", encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.header.keys())
            for row in reader:
                # Check if row satisfies all conditions.
                if all(row[key] == val for key, val in filter.items()):
                    print(" ".join(row.values()))


book = PhoneBook("phone_book.csv")

# book.edit_row("+75867436683", {"Имя": "buba"})
book.print_page(1)
# book.find()
book.add_new_row(["a", "a", "a", "a", "a", "a"])
