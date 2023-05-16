import subprocess

subprocess.run(["python", "shiftexchrequest_add.py"]) #создание заявки на биржу
subprocess.run(["python", "shiftexchrequest_create_respond.py"]) #отклик на заявку на биржу
subprocess.run(["python", "shiftexchrequest_confirm_request.py"]) # Подтверждение заявки с биржы
subprocess.run(["python", "shiftexchrespond_cancel_respond.py"]) # Отмена отклика с биржы
subprocess.run(["python", "shiftexchrequest_delete.py"]) # Удаление заявки с биржы
subprocess.run(["python", "shiftexchrequest_import.py"]) #импорт заявки с биржы
subprocess.run(["python", "shiftexchrequest_cancel_request.py"]) #Отмена заявки с биржы
subprocess.run(["python", "shiftexchrequest_delete.py"]) # Удаление заявки с биржы
subprocess.run(["python", "shiftexchrequest_add.py"]) #создание заявки на биржу
subprocess.run(["python", "shiftexchrequest_create_respond.py"]) #отклик на заявку на биржу
subprocess.run(["python", "shiftexchrequest_confirm_absence.py"]) #Подтверждение неявки на заявку с биржы
subprocess.run(["python", "shiftexchrespond_delete.py"]) #Удаление отклика с биржы
subprocess.run(["python", "shiftexchrequest_add.py"]) #создание заявки на биржу
subprocess.run(["python", "shiftexchrequest_create_respond.py"]) #отклик на заявку на биржу
subprocess.run(["python", "shiftexchrespond_change_user.py"]) #Изменение пользователя в отклике
subprocess.run(["python", "agencyoutsource_add.py"]) #Добавление аутсорс агенства
subprocess.run(["python", "agencyoutsource_delete.py"]) #Удаление аутсорс агенства
subprocess.run(["python", "workregime_add.py"]) #Добавление режима работы
subprocess.run(["python", "workregime_delete.py"]) #Удаление режима работы
subprocess.run(["python", "workerday_add.py"]) #Добавление календаря по режимам работы
subprocess.run(["python", "workerday_import.py"]) #Импорт календаря по режимам работы
subprocess.run(["python", "workplan_add.py"]) #Добавление планирования
subprocess.run(["python", "workplan_confirm.py"]) #Утверждение планирования
subprocess.run(["python", "workplan_delete.py"]) #Удаление планирования
subprocess.run(["python", "workperiod_add.py"]) #Добавление занятости по дням
subprocess.run(["python", "workperiod_import.py"]) #Импорт занятости по дням
subprocess.run(["python", "workperiod_delete.py"]) #Удаление занятости по дням
subprocess.run(["python", "absencetype_add.py"]) #Добавление типа отсутсвия
subprocess.run(["python", "absence_add.py"]) #Добавление отсутсвия




