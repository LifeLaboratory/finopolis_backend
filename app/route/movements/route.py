# coding=utf-8
from app.route.movements.processor import *
from app.api.base.base_router import BaseRouter
from app.api.base import base_name as names


class Movement(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.it, names.date_time, names.qty, names.movement,
                     names.nom_price, names.face, names.face_id]

    def get(self):
        self._read_args()
        answer = get_movements(self.data)
        return answer or {}

    def post(self):
        self._read_args()
        answer = []
        if self.data.get(names.movement):
            for mov in self.data.get(names.movement):
                answer = insert_movement(mov)
        return answer or {}
