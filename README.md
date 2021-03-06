# Космический instagram

Скрипты позволяют скачивать изображения из репозитариев SpaceX и Hubble, а затем публиковать их в instagram.

Пакет состоит из трёх независимых скриптов:
1. `fetch_spacex.py`
2. `fetch_hubble.py`
3. `instapost.py`

## Как установить

Python3 должен быть уже установлен в системе.  
Используя `pip` или  `pip3`  (если есть конфликт с python2) необходимо установить  зависимости:

```shell
pip install -r requirements.txt
```

Рекомендуется использовать виртуальное окружение для изоляции проекта.  
Подробности: [virtualenv/venv](https://docs.python.org/3/library/venv.html).

### Настройка имени и пароля для instagram

Если у вас еще нет аккаунта в instagram, зарегистрироваться [здесь](https://instagram.com)
После получения имени и пароля необходимо добавить их в файл `.env` в директории со скриптами.

В файле  `.env` написать две строки такого вида:

```
LOGIN_INSTA=ВАШ_ЛОГИН
PASS_INSTA=ВАШ_ПАРОЛЬ
```

## Как пользоваться скриптами

### fetch_spacex.py

Скрипт предназначен для скачивания изображений с последнего запуска.

В текущей директории будет создана папка images, куда будут сохранены все фотографии с последнего запуска SpaceX. Файлы будут иметь имена вида: spacexX.jpg, где X - цифра.

**Запуск**

```shell
python3 fetch_spacex.py
```

Выполнение может потребовать некоторое время. Если всё прошло хорошо, в текущей директории создастся папка `images`, в которую будут сохранены полученный файлы

### fetch_hubble.py
Скрипт скачивает файлы из коллекций Hubble.
Коллекций достаточно много, например: `wallpaper`, `news`, `spacecraft`, `holiday_cards`, `printshop`, `stsci_gallery` и другие. Этот список никак не регламентирован и он может пополняться как угодно. Если заданная коллекция существует - скрипт скачает изображения.

**Запуск**

```shell
python3 fetch_hubble.py wallpaper
```
Вместо `wallpepers` можно указать любую коллекцию.
Скрипт получает все файлы данной коллекции и скачивает изображения в текущую директорию `images`.

### instapost.py
Скрипт предназначен для подготовки файлов к публикации с дальнейшем публикацией в заданном аккаунте instagram (аккаунт задавали в файле `.env`)

**Запуск**
```shell
python3 instapost.py
```

После запуска все изображения из директории `images` будут обрезаны до квадратного вида 1080px X 1080px. Нужное изображение вырезается из середины.
Далее идёт загрузка изображений в инстаграм.

*Внимание!* Не все фотографии могут быть загружены по разным причинам, например: не верный тип фото. О ходе загрузки будет указано в консоли.

## Цель проекта
Данные скрипты написаны только с образовательной целью. 