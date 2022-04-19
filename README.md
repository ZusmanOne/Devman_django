# Яндекс афиша



## Запуск

Для запуска проекта у вас уже должен быть установлен Python 3.

- Скачайте код 
```console 
 git clone https://github.com/ZusmanOne/Devman_django.git
  ```
- создайте виртуальное окружение командой
```console
mkvirtualenv 'venvname'
```
- Установите зависимости командой
```console
  pip install -r requirements.txt
````
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` 
и запишите туда данные(SECRET_KEY, DEBUG) из settings.py в таком формате: `ПЕРЕМЕННАЯ=значение`. 
 
- Примените миграции для БД:
```console
python manage.py migrate 
````

- Запустите сервер командой `python3 manage.py runserver`

По адресу http://zusmanone.pythonanywhere.com/ есть демо-версия приложения, для доступа к панели админа
по адресу http://zusmanone.pythonanywhere.com/admin введите логин/пароль:
- ``devman``
- ``devman``

Так же проект имеет доп. функционал в виде загрузки местоположений через консоль, для этого введите в консоль:
``python manage.py load_place адрес.json(url адрес на json-файл) ``
для примера используйте этот адрес:
https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
Приложение загрузит объект в БД и отобразит на главной странице

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

