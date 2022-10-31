# Проект для сдачи экзамена по дисциплине "Защита информации"

Api-приложение с регистрацией и авторизацией. В личном кабинете доступны функции шифрования и удаления пользователей

### Установка зависимостей

    pip install -r requirements.txt

### Запуск приложения

    app.py -p

# Описание проекта

## Главная страница

    /main/

Пользователю предлагается пройти регистрацию или авторизоваться

![main_page](https://github.com/R0ryMercury/information_security/blob/master/readme_files/main.png)

## Страница регистрации

    /auth/register/

Чтобы пройти регистрацию пользователь должен заполнить поля отмеченные
После этого он добавится в бд и сможет авторизоваться используя указанные логин и пароль

![registration_page](https://github.com/R0ryMercury/information_security/blob/master/readme_files/registration.png)

## Страница авторизации

    /auth/login/

На данной странице пользователь может авторизоваться и попасть в своей личный кабинет

![login_page](https://github.com/R0ryMercury/information_security/blob/master/readme_files/login.png)

## Личный кабинет

    /user/profile/

Выводится вся информация о пользовтеле, также можно произвести шифровку разного вида, если это профиль пользователя с ролью админ, доступна кнопка "управление пользователями"

![profile_page](https://github.com/R0ryMercury/information_security/blob/master/readme_files/profile.png)

## Стеганография

![stegano](https://github.com/R0ryMercury/information_security/blob/master/readme_files/img_ciphre.gif)

## Шифр цезаря

![caesar_ciphre](https://github.com/R0ryMercury/information_security/blob/master/readme_files/caesar_ciphre.gif)

## Управление пользователями

Позволяет удалить любого пользователя с ролью "user"

![user_management](https://github.com/R0ryMercury/information_security/blob/master/readme_files/user_management.gif)
