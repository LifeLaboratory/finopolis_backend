# coding=utf-8
from app.route.nomenclature.processor import *
from app.api.base.base_router import BaseRouter
from app.api.base import base_name as names


class Nomenclature(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.post_id, names.post_title, names.post_text, names.face_id, names.nom_name, names.nom_text,
                     names.nom_price, names.nom_category, names.face,
                     names.post_photo, names.it, names.date_time, names.post_deleted, names.post_draft]

    def get(self):
        self._read_args()
        answer = get_nomenclature(self.data)
        return answer or {}

    def post(self):
        self._read_args()
        answer = update_nomenclature(self.data)
        return answer or {}
