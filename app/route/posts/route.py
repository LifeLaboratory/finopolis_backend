# coding=utf-8
from app.route.posts.processor import *
from app.api.base.base_router import BaseRouter
from app.api.base import base_name as names


class Posts(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.post_id, names.post_title, names.post_text,
                     names.post_photo, names.it, names.date_time, names.post_deleted, names.post_draft]

    def get(self):
        self._read_args()
        answer = get_post(self.data)
        return answer or {}

    def post(self):
        self._read_args()
        answer = update_post(self.data)
        return answer or {}
