import subprocess

subprocess.run(["python", "timesheet_add.py"]) #Добавление табеля
subprocess.run(["python", "timesheet_import.py"]) #Импорт табеля
subprocess.run(["python", "timesheet_delete.py"]) #Удаление записи в табеле
subprocess.run(["python", "timesheet_fill.py"]) #Перерасчет в табеле