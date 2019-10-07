from app.route.posts.provider import Provider
from app.api.base import base_name as names
from datetime import datetime as dt

def get_post(args):
    answer = None
    provider = Provider()
    if args.get(names.post_id):
        answer = provider.get_post(args)
        if answer:
            answer = answer[0]
            if answer.get(names.date_time):
                answer[names.date_time] = answer.get(names.date_time).strftime("%Y-%m-%d %H:%M")
            get_nomenclature(answer)
    elif args.get(names.face_id):
        answer = provider.get_all_post(args)
        if answer:
            for ans in answer:
                if ans.get(names.date_time):
                    ans[names.date_time] = ans.get(names.date_time).strftime("%Y-%m-%d %H:%M")
                get_nomenclature(ans)
    return answer or {}


def get_nomenclature(data):
    nomenclature = {}
    for field in names.nom_field:
        nomenclature[field] = data.get(field)
        data.pop(field)
        data['товар'] = nomenclature


def update_post(args):
    provider = Provider()
    for field in names.post_fields:
        if args.get(field) is None:
            if field in names.date_time_fields:
                args[field] = dt.now()
            else:
                args[field] = 'NULL'
    if args.get(names.post_id):
        answer = provider.update_post(args)[0]
    else:
        answer = provider.create_post(args)[0]
    return answer
