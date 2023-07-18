from main.models import Client
import re


def get_distinct_activities():
    temp_list = []
    queryset = Client.objects.values_list('activity', flat=True)
    for el in queryset:
        el = el.replace("{", "").replace("}", "").replace('"', "").replace(", ", ' ').replace("Інш", " Інш").replace(
            "Індив", " Індив").replace("Індивідуальна творча діяльність", '').replace(
            "Інший пасажирський наземний транспорт",
            '')
        elements = el.split(",")

        for _ in elements:
            if "Інші" in _:
                updated_activity = re.sub(r"\bІнші\b.*", "", _)
                temp_list.append(updated_activity.strip())
            else:
                temp_list.append(_)
    return sorted(list(set(temp_list)))
