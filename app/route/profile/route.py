# coding=utf-8
from app.api.base import base_name as names
from app.route.profile.processor import *
from app.api.base.base_router import BaseRouter


class Profile(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.FIO, names.DESCRIPTION, names.PHOTO, names.STATUS]

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_profile(args)
        return answer or {}

    def put(self, id_user):
        self._read_args()
        self.data.update({names.ID_USER: id_user})
        print(self.data)
        answer = update_profile(self.data)
        return answer or {}
