import subprocess

subprocess.run(["python", "shiftexchrequest_add_without_plan.py"]) #проверка что заяка не создается, если план на текущий месяц не создан по данной точке
subprocess.run(["python", "workplan_add_for_andrew3.py"]) #создание плана для подписчика andrew3
subprocess.run(["python", "shiftexchrequest_add_with_bid.py"]) #Создание заявки на биржу со ставкой вручную
subprocess.run(["python", "сheck_shiftexchrequest_has_not_been_deleted.py"]) #Тест при проставлении отсутсвия заявка по которой был отклик в бирже не удаляеться из занятости по дням, время высвобождаеться, в занятости по дням проставляеться тип отсуствия