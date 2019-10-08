from app.route.movements.provider import Provider
from app.api.base import base_name as names
import json


def get_movements(args):
    provider = Provider()
    answer = provider.get_movements(args)
    for ans in answer:
        if ans.get(names.date_time):
            ans[names.date_time] = ans.get(names.date_time).strftime("%Y-%m-%d %H:%M")
    return answer


def insert_movement(args):
    provider = Provider()
    answer = provider.insert_into_movements(args)[0]
    return answer
