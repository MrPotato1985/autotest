import subprocess

subprocess.run(["python", "timesheet_add.py"]) #Добавление табеля
subprocess.run(["python", "timesheet_import.py"]) #Импорт табеля
subprocess.run(["python", "timesheet_delete.py"]) #Удаление записи в табеле
subprocess.run(["python", "timesheet_fill.py"]) #Перерасчет в табеле
subprocess.run(["python", "timesheet_approve.py"]) #Уиверждение в табеле

subprocess.run(["python", "worktimefact_add.py"]) #Добавление фактического отработанного времени
subprocess.run(["python", "worktimefact_delete.py"]) #Удаление фактического отработанного времени
subprocess.run(["python", "worktimefact_import.py"]) #Импорт фактического отработанного времени

subprocess.run(["python", "worktimelog_add.py"]) #Добавление журнала рабочего времени