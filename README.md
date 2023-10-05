# repository_for_hard_qode
полный проект для миниэкзамена в компанию HardQode





class TestCategorys - класс тестов категории

    test_get_category. Тест - получить список всех видов животных

    test_post_category. Тест создаёт категорию животного с уникальным названием.

    test_get_category_by_ID. Тест - получить категорю животного по ID

    test_put_category_by_ID(self). Тест - обновить категорию животного. Название должно быть уникальным.
        
    test_delete_category_by_ID. Тест - Удалить категорию животных.
        

class TestPens - класс тестов животных.

    test_get_pen. Тест - получить список всех животных

    test_create_category. Создание временной категории для создания в ней животного.
        
    test_post_pen. Тест - создаёт животного с уникальным название


    test_get_pet_by_ID. Тест - получить название животного по ID
    
    test_put_pet_by_ID. Тест - обновить категорию животного. Название должно быть уникальным.
        
    test_delete_pet_by_ID. Тест - Удалить категорию животных по ID.
        
    test_delete_category_by_ID. Тест - удалить категорию животного, созданную для тестов.
       

class TestToken - класс тестирования токенов.
    test_post_token - отправка токена на сайт. 
       

команда для запуска теста:

  pytest --html=report.html --self-contained-html test_hardcode.py