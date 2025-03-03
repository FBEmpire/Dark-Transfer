import requests
import base64
import os

mode = input("mode (1 - upload; 2 - download): ")

if mode == '1':
    name = input("filename: ")
elif mode == '2':
    table = input("tablename: ")
else:
    print("Invalid mode selected.")
    exit()

def upload_image(file_path):
       with open(file_path, 'rb') as img_file:
           base64_data = base64.b64encode(img_file.read()).decode('utf-8')
       
       response = requests.post('http://fbe.leyixgame.ru:5000/upload', json={'image': base64_data})
       
       try:
           print(response.json())
       except ValueError:
           print("Response content is not valid JSON:", response.text)

def download_images(table_name):
    response = requests.post('http://fbe.leyixgame.ru:5000/download', json={'table_name': table_name})

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
