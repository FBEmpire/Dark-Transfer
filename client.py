import requests
import base64
import os
import platform

os_name = platform.system()

print(os_name)
if os_name == "Linux":
    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')


clear()

print("                                _____                                           ")
print("                               |     \    \     /                               ")
print("                               |      |    \   /                                ")
print("                               |_____/      \ /                                 ")
print("                               |     \       |                                  ")
print("                               |      |      |                                  ")
print("                               |_____/       |                                  ")
print("                                                                                ")
print("                                                                                ")
print("                                                                                ")
print(" ______      ______                         _____        _______                ")
print("|           |           |\          /|     |     \      /       \        \     /")
print("|           |           | \        / |     |      |    |         |        \   / ")
print("|______     |______     |  \      /  |     |_____/     |         |         \ /  ")
print("|           |           |   \    /   |     |     \     |         |          |   ")
print("|           |           |    \  /    |     |      |    |         |          |   ")
print("|           |______     |     \/     |     |_____/      \ _____ /           |   ")
print("                                                                                ")
print("                                                                                ")
print("          ______                     _____          _____      ______           ")
print("         |         |\          /|   |     \    |   |     \    |                 ")
print("         |         | \        / |   |      |   |   |      |   |                 ")
print("         |______   |  \      /  |   |_____/    |   |_____/    |______           ")
print("         |         |   \    /   |   |          |   |   \      |                 ")
print("         |         |    \  /    |   |          |   |    \     |                 ")
print("         |______   |     \/     |   |          |   |     \    |______           ")
print("                                                                                   site: fbe.leyixgame.ru")

# Запрос режима работы
mode = input("mode (1 - upload; 2 - download): ")

if mode == '1':
    # Запрос логина, пароля и секретного кода только для загрузки
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    secret_key = input("Введите секретный код: ")
    # Проверка авторизации
    auth_response = requests.post('http://sql.leyixgame.ru:5000/auth', json={
        'username': username,
        'password': password,
        'secret_key': secret_key
    })
  
    if auth_response.status_code != 200:
        print("Ошибка авторизации:", auth_response.json().get('error', 'Неизвестная ошибка'))
        exit()

    print("Авторизация успешна!")

    # Запрос имени файла для загрузки
    name = input("filename: ")
elif mode == '2':
    # Запрос имени таблицы для скачивания
    table = input("tablename: ")
else:
    print("Invalid mode selected.")
    exit()

def upload_image(file_path):
    # Извлечение формата файла
    file_format = file_path.split('.')[-1]  # Получаем расширение файла
    with open(file_path, 'rb') as img_file:
        base64_data = base64.b64encode(img_file.read()).decode('utf-8')  # Преобразуем файл в base64
    
    # Отправка данных на сервер
    response = requests.post('http://sql.leyixgame.ru:5000/upload', json={
        'auth': {
            'username': username,
            'password': password,
            'secret_key': secret_key
        },
        'image': base64_data,
        'file_format': file_format
    })
    
    try:
        print(response.json())
    except ValueError:
        print("Response content is not valid JSON:", response.text)

def download_images(table_name):
    # Отправка данных на сервер для скачивания
    response = requests.post('http://sql.leyixgame.ru:5000/download', json={
        'table_name': table_name
    })

    if response.status_code == 200:
        # Сохраняем файл на клиенте
        filename = response.headers.get('Content-Disposition').split('filename=')[1].strip('"')
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image saved as: {filename}")
    else:
        print("Error:", response.json())

if __name__ == '__main__':
    if mode == '1':
        upload_image(name)
    elif mode == '2':
        download_images(table)
