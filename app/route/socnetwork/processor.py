from app.route.socnetwork.provider import Provider
from app.api.base import base_name as names


def get_socnetwork(args):
    provider = Provider()
    if args.get(names.socnet):
        answer = provider.get_socnetwork(args)
    else:
        answer = provider.get_all_socnetwork()
    return answer

def update_socnetwork(args):
    provider = Provider()

    if args.get(names.socnet):
        answer = provider.update_socnetwork(args)
    else:
        answer = provider.create_socnetwork(args)
    return answer
