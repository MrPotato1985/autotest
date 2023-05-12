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

