import subprocess

subprocess.run(["python", "shiftexchrequest_add.py"]) #создание заявки на биржу
subprocess.run(["python", "shiftexchrequest_create_respond.py"]) #отклик на заявку на биржу
subprocess.run(["python", "shiftexchrequest_confirm_request.py"]) # Подтверждение заявки с биржы
subprocess.run(["python", "shiftexchrequest_delete.py"]) # Удаление заявки с биржы
subprocess.run(["python", "shiftexchrequest_confirm_absence.py"]) #Подтверждение неявки на заявку с биржы




