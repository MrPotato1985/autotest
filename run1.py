import subprocess

subprocess.run(["python", "shiftexchrequest_add+2d.py"]) #создание заявки на биржу
subprocess.run(["python", "shiftexchrequest_create_respond.py"]) #отклик на заявку на биржу
subprocess.run(["python", "shiftexchrespond_change_user.py"]) #Изменение пользователя в отклике