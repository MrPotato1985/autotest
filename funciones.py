import inspect
import os
import pyautogui

# функция добавления в текстовый файл текс + имя файла
def agregar_archivo(file_name, text):
    with open(file_name, 'a') as file:
        caller_frame = inspect.stack()[1]
        caller_filename = os.path.basename(caller_frame.filename)
        file.write(text + " " + caller_filename)

# создание скриншота
def capture_screenshot():
    # Получение имени файла вызывающего скрипта
    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename
    caller_script_name = os.path.splitext(os.path.basename(caller_filename))[0]

    # Создание имени файла скриншота
    filename = f"{caller_script_name}_screenshot.png"

    # Создание скриншота экрана и сохранение в файл
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)



