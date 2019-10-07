# coding=utf-8
from app.route.socnetwork.processor import *
from app.api.base.base_router import BaseRouter
from app.api.base import base_name as names


class Socnetwork(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.nom_name, names.LOGIN, names.PASSWORD, names.LINK, names.socnet]

    def get(self):
        self._read_args()
        answer = get_socnetwork(self.data)
        return answer or {}

    def put(self):
        self._read_args()
        answer = update_socnetwork(self.data)
        return answer or {}
