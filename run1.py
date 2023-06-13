import subprocess

subprocess.run(["python", "shiftexchrequest_add_without_plan.py"]) ##проверка что заяка не создается, если план на текущий месяц не создан по данной точке
subprocess.run(["python", "workplan_add_for_andrew3.py"]) #создание плана для подписчика andrew3
subprocess.run(["python", "shiftexchrequest_add_with_bid.py"]) #Создание заявки на биржу со ставкой вручную