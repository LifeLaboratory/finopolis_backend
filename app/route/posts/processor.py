from app.route.posts.provider import Provider
from app.api.base import base_name as names


def get_post(args):
    provider = Provider()
    if args.get(names.post_id):
        answer = provider.get_post(args)[0]
        if answer.get(names.date_time):
            answer[names.date_time] = answer.get(names.date_time).strftime("%Y-%m-%d %H:%M")
    else:
        answer = provider.get_all_post(args)
        for ans in answer:
            if ans.get(names.date_time):
                ans[names.date_time] = ans.get(names.date_time).strftime("%Y-%m-%d %H:%M")
    return answer


def update_post(args):
    provider = Provider()
    if args.get(names.post_id):
        answer = provider.update_post(args)[0]
    else:
        answer = provider.create_post(args)[0]
    return answer
