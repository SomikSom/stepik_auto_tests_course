import os

# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'null.txt')  # добавляем к этому пути имя файла
# element.send_keys(file_path)
print(file_path)