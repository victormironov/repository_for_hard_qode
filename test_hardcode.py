from pprint import pprint as pp
import requests

BASE_LINK = "http://91.210.171.73:8080/api"


class TestCategorys():

    def test_get_category(self):
        """
        тест - получить список всех видов животных

        """
        r = requests.get(BASE_LINK + '/category/', auth=('admin', 'admin'))

        assert r.status_code == 200, f"код ошибки = {r.status_code}"

    def test_post_category(self):
        """
        Тест создаёт категорию животного с уникальным название

        """
        p = requests.post(BASE_LINK + '/category/', data={'name': 'unicorn1'}, auth=('admin', 'admin'))
        global ID
        ID = p.json()['id']
        print("ID =", ID)
        assert p.status_code == 201, f"код ошибки = {p.status_code}"

    def test_get_category_by_ID(self):
        """
        Тест - получить категорю животного по ID

        """

        p = requests.get(BASE_LINK + f'/category/{ID}', auth=('admin', 'admin'))
        print(p.json())
        assert p.status_code == 200, f"код ошибки = {p.status_code}"

    def test_put_category_by_ID(self):
        """
        Тест - обновить категорию животного. Название должно быть уникальным.
        """
        p = requests.put(BASE_LINK + f'/category/{ID}', data={'name': 'bicorn'},
                         auth=('admin', 'admin'))

        assert p.status_code == 200, f"код ошибки = {p.status_code}"

    def test_delete_category_by_ID(self):
        """
        Тест - Удалить категорию животных
        """
        d = requests.delete(BASE_LINK + f'/category/{ID}', auth=('admin', 'admin'))

        assert d.status_code == 204, f"код ошибки = {d.status_code}"


class TestPens():

    def test_get_pen(self):
        """
        тест - получить список всех животных

        """
        r = requests.get(BASE_LINK + '/pet/', auth=('admin', 'admin'))
        # pp(r.json())
        assert r.status_code == 200, f"код ошибки = {r.status_code}"

    def test_create_category(self):
        p = requests.post(BASE_LINK + '/category/', {'name': 'horned'}, auth=('admin', 'admin'))
        global ID
        ID = p.json()['id']
        # print("ID =", ID)
        assert p.status_code == 201, f"код ошибки = {p.status_code}"

    def test_post_pen(self):
        """
        Тест создаёт животного с уникальным название

        """

        pc = requests.post(BASE_LINK + '/pet/',
                           {
                               "category": {
                                   "name": "horned"
                               },
                               "name": "unicorn",
                               "photo_url": "string",

                               "status": "available"
                           },
                           auth=('admin', 'admin'))

        assert pc.status_code == 201, f"код ошибки = {pc.status_code}"

    def test_get_pet_by_ID(self):
        """
        Тест - получить название животного по ID

        """

        p = requests.get(BASE_LINK + '/pet/128', auth=('admin', 'admin'))
        print(p.json())
        assert p.status_code == 200, f"код ошибки = {p.status_code}"

    def test_put_pet_by_ID(self):
        """
        Тест - обновить категорию животного. Название должно быть уникальным.
        """
        p = requests.put(BASE_LINK + '/pet/128', data={'id': 128, 'name': 'Turzik',
                                                       'photo_url': 'WWW.Photo2.Com',
                                                       'category': {'id': 478, 'name': 'cats'},
                                                       'status': 'available'}, auth=('admin', 'admin'))

        assert p.status_code == 200, f"код ошибки = {p.status_code}"

    def test_delete_pet_by_ID(self):
        """
        Тест - Удалить категорию животных
        """
        d = requests.delete(BASE_LINK + '/pet/128', auth=('admin', 'admin'))

        assert d.status_code == 204, f"код ошибки = {d.status_code}"

    def test_delete_category_by_ID(self):
        """
        Тест - удалить категорию животного, созданную для тестов
        """
        d = requests.delete(BASE_LINK + f'/category/{ID}', auth=('admin', 'admin'))
        # print('status_code =', d.status_code )
        assert d.status_code == 204, f"код ошибки = {d.status_code}"


class TestToken():
    def test_post_token(self):
        p = requests.post(BASE_LINK + '/token/auth/',
                          json={"username": "simple_name", "password": "simple_password"},
                          auth=('admin', 'admin'))
        assert p.status_code == 200, f"код ошибки = {p.status_code}"
