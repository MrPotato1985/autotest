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
subprocess.run(["python", "workregime_add.py"]) #Добавление режима работы
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
subprocess.run(["python", "absence_import.py"]) #Импорт отсутсвия
subprocess.run(["python", "absence_delete.py"]) #Удаление отсутсвия
subprocess.run(["python", "presencetype_add.py"]) #Добавление типа присутсвия
subprocess.run(["python", "presencetype_delete.py"]) #Удаление типа присутсвия
subprocess.run(["python", "budgetfot_add.py"]) #Добавление лимит ФОТ
subprocess.run(["python", "budgetfot_delete.py"]) #Удаление лимита ФОТ
subprocess.run(["python", "budgetfot_import.py"]) #импорт лимита ФОТ
subprocess.run(["python", "worktimefund_add.py"]) #Добавление  ФРВ по ТТ
subprocess.run(["python", "worktimefund_delete.py"]) #Удаление ФРВ по ТТ
subprocess.run(["python", "worktimefund_import.py"]) #импорт ФРВ по ТТ
subprocess.run(["python", "additionalstaffagreement_add.py"]) #Добавление Доп. часы по ТТ
subprocess.run(["python", "additionalstaffagreement_delete.py"]) #Удаление Доп. часы по ТТ
subprocess.run(["python", "worktimeschedulelimits_add.py"]) #Добавление правила и ограничения
subprocess.run(["python", "worktimeschedulelimits_delete.py"]) #Удаление правила и ограничения