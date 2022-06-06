import os
import time

#Путь к каталогу
path = f'C:\\Users\\{os.getlogin()}\\Downloads'

#Названия расширений
expansions = {
    "image": ['.jpg', '.png', '.ico', '.gif'],
    "video": ['.mp4', '.webm'],
    "torrent": ['.torrent'],
    "installer": ['.exe', '.bat'],
    "audio": ['.mp3', '.wav'], 
    "document": ['.doc', '.docx', '.pptx', '.pdf', '.xlsx', '.txt'],
    "archive": ['.zip', '.rar']
}

list_catalog = ["Images", "Torrents", "Installers", "Sounds", "Videos", "Archives", "Documents"]

#Функция перемещения файла по папкам
def moving_file(folder, file):
    if not os.path.exists(f'{path}\\{folder}\\{"".join(file)}'):
        print("Перемещение в папку {}': {}".format(folder, ''.join(file)))
        os.rename(f'{path}\\{"".join(file)}', f'{path}\\{folder}\\{"".join(file)}')
    else: 
        print("Файл с таким именем уже находится в папке!!!")

#Функция проверки на существование папок
def check_catalog():
    for name_catalog in list_catalog:
        path_catalog = f'{path}\\{name_catalog}'
        if not os.path.isdir(path_catalog):
            os.mkdir(path_catalog)
            print("Такой папки не существовало и она была создана!")
        else:
            print("Такая папка существует)")

#Файл-мессенджер
def file_messendger():
    while True:
        time.sleep(5)
        name_files = []
        content_catalog = os.listdir(path=path)
        for content in content_catalog:
            name_files.append(os.path.splitext(content))
        for expansion in name_files:
            if len(expansion) > 1:
                if expansion[1] in expansions['image']:
                    moving_file("Images", expansion)
                elif expansion[1] in expansions['torrent']:
                    moving_file("Torrents", expansion)
                elif expansion[1] in expansions['installer']:
                    moving_file("Installers", expansion)
                elif expansion[1] in expansions['audio']:
                    moving_file("Sounds", expansion)
                elif expansion[1] in expansions['video']:
                    moving_file("Videos", expansion)
                elif expansion[1] in expansions['archive']:
                    moving_file("Archives", expansion)
                elif expansion[1] in expansions['document']:
                    moving_file("Documents", expansion)
                else:
                    print("Остается на месте {}".format(''.join(expansion)))

def main():
    check_catalog()
    time.sleep(2)
    file_messendger()

if __name__ == "__main__":
    main()