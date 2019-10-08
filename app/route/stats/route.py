# coding=utf-8
from app.route.stats.processor import *
from app.api.base.base_router import BaseRouter
from app.api.base import base_name as names


class Stats(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.face, names.post, names.socnet, names.likes, names.views, names.comments]

    def get(self):
        self._read_args()
        print(self.data)
        answer = get_stat(self.data)
        return answer or {}

    def put(self):
        self._read_args()
        answer = update_stat(self.data)
        return answer or {}
