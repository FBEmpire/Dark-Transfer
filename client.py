#        ______      ______                         _____        _______                
#       |           |           |\          /|     |     \      /       \        \     /       #
#       |           |           | \        / |     |      |    |         |        \   /        #
#       |______     |______     |  \      /  |     |_____/     |         |         \ /         #
#       |           |           |   \    /   |     |     \     |         |          |          #
#       |           |           |    \  /    |     |      |    |         |          |          #
#       |           |______     |     \/     |     |_____/      \ _____ /           |          #
#                                                                                              #
#                                                                                              #
#                 ______                     _____          _____      ______                  #
#                |         |\          /|   |     \    |   |     \    |                        #
#                |         | \        / |   |      |   |   |      |   |                        #
#                |______   |  \      /  |   |_____/    |   |_____/    |______                  #
#                |         |   \    /   |   |          |   |   \      |                        #
#                |         |    \  /    |   |          |   |    \     |                        #
#                |______   |     \/     |   |          |   |     \    |______                  #



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
       
       response = requests.post('http://sql.leyixgame.ru:5000/upload', json={'image': base64_data})
       
       try:
           print(response.json())
       except ValueError:
           print("Response content is not valid JSON:", response.text)

def download_images(table_name):
    response = requests.post('http://sql.leyixgame.ru:5000/download', json={'table_name': table_name})

    if response.status_code == 200:
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
