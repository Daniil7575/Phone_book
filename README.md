# Phone_book

## main.py

В данном файле представлен класс телефонной книги.


### HEADER - глобадьная переменная, хранящая названия столбцов в csv файле
---

### def _get_page - служебный метод, возвращает указанныю страницу с записями
---

### def print_page - метод для вывода в консоль страницы с указанным номером
Пример:
```
book = PhoneBook("phone_book.csv")

# в консоль будет напечатана вторая страница (страницы начинаются с 1)
book.print_page(2)
```
---

### def add_new_row - метод для добавления новой записи в файл

Пример:
```
book = PhoneBook("phone_book.csv")

# будет создана запись со значениями "a" во всех столбцах
book.add_new_row(["a", "a", "a", "a", "a", "a"])
```
---

### def _deltmp - служебный метод для удаления временного файла
---

### def edit_row - изменить указанные параметры записи на новые указанные значения по данному личному номеру телефона

Пример:
```
book = PhoneBook("phone_book.csv")

# будет изменено имя на "Иван", а органиация на "111" у записи с личным номером "+75867436683"
book.edit_row("+75867436683", {"Имя": "Иван", "Организация": "111"})
```
---

### def find - найти строки по фильтру (фильтр представляет собой словарь из имен столбцов и их значений, по которым будет осуществляться поиск) и вывести их в консоль

Пример:
```
book = PhoneBook("phone_book.csv")

# будут выведены все записи, с именем "Иван" и фамилией "Иванов"
book.find({"Имя": "Иван", "Фамилия": "Иванов"})
```

## data_generator.py

Необязательный генератор заполненных csv файлов, для его работы потребуется установить библиотеки, указанные в **requirements.txt** в виртуальное окружение.

```
pip install -r requirements.txt
```

P.S. Это можно было сделать с помощью pandas.
