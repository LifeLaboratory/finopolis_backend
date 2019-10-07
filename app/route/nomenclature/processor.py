from app.route.nomenclature.provider import Provider
from app.api.base import base_name as names


def get_nomenclature(args):
    provider = Provider()
    if args.get(names.nom_id):
        answer = provider.get_nomenclature(args)
        if answer:
            answer = answer[0]
    else:
        answer = provider.get_all_nomenclature(args)
    return answer


def update_nomenclature(args):
    provider = Provider()
    if args.get(names.nom_id):
        answer = provider.update_nomenclature(args)[0]
    else:
        answer = provider.create_nomenclature(args)[0]
    return answer
