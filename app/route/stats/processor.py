from app.route.stats.provider import Provider
from app.api.base import base_name as names


def get_stat(args):
    provider = Provider()
    if args.get(names.face):
        answer = provider.get_stat_by_face(args)
    elif args.get(names.post):
        answer = provider.get_stat_by_post(args)
    else:
        answer = provider.get_all_stat()
    return answer

def update_stat(args):
    provider = Provider()

    if args.get(names.STATS_POSTS_ID):
        answer = provider.update_stat(args)
    else:
        answer = provider.create_stat(args)
    return answer


#Доделать всё.
