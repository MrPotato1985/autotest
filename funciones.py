import inspect
import os

# функция добавления в текстовый файл текс + имя файла
def agregar_archivo(file_name, text):
    with open(file_name, 'a') as file:
        caller_frame = inspect.stack()[1]
        caller_filename = os.path.basename(caller_frame.filename)
        file.write(text + " " + caller_filename)


