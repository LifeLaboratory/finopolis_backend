import unittest
from app.route.posts import processor as post_processor
from app.route.nomenclature import processor as nom_processor
from app.api.base import base_name as names


class TestPosts(unittest.TestCase):
    def test_post(self):

        data = {
            names.face_id: 1
        }
        answer = post_processor.get_post(data)
        data[names.post_id] = answer[0].get(names.post_id)

        data = {
            names.post_title: 'test',
            names.post_text: 'test',
            names.post_photo: 'test',
            names.it: '1',
            names.date_time: '2019-10-07 14:09',
            names.post_deleted: False,
            names.post_draft: False,
            names.face: 1,
            names.face_id: 1
        }
        answer = post_processor.update_post(data)
        post_id = answer.get(names.post_id)
        self.assertIsNotNone(post_id)
        data[names.post_id] = post_id
        data[names.post_deleted] = True
        answer = post_processor.update_post(data)
        answer = post_processor.get_post(data)
        return

    def test_nomenclature(self):
        data = {
            names.face_id: 3
        }
        answer = nom_processor.get_nomenclature(data)
        data[names.post_id] = answer[0].get(names.post_id)

        data = {
            names.nom_name: 'test',
            names.nom_text: 'test',
            names.nom_category: 'test',
            names.nom_price: '100',
            names.nom_photo: '123',
            names.face: 1,
            names.post_deleted: False,
            names.face_id: 1
        }
        answer = nom_processor.update_nomenclature(data)
        nom_id = answer.get(names.nom_id)
        self.assertIsNotNone(nom_id)
        data[names.post_id] = nom_id
        data[names.post_deleted] = True
        answer = nom_processor.update_nomenclature(data)
        answer = nom_processor.get_nomenclature(data)
        return
