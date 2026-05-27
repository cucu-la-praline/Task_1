from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def setup_method(self):
        """Подготовка данных для каждого теста"""
        self.database = Database()

    def test_database_initialization_has_buns(self):
        """Тест инициализации базы данных с булочками"""
        buns = self.database.available_buns()

        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    def test_database_initialization_has_ingredients(self):
        """Тест инициализации базы данных с ингредиентами"""
        ingredients = self.database.available_ingredients()

        assert len(ingredients) == 6

    def test_database_has_sauces(self):
        """Тест наличия соусов в базе данных"""
        ingredients = self.database.available_ingredients()
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]

        assert len(sauces) == 3
        assert sauces[0].get_name() == "hot sauce"
        assert sauces[0].get_price() == 100
        assert sauces[1].get_name() == "sour cream"
        assert sauces[1].get_price() == 200
        assert sauces[2].get_name() == "chili sauce"
        assert sauces[2].get_price() == 300

    def test_database_has_fillings(self):
        """Тест наличия начинок в базе данных"""
        ingredients = self.database.available_ingredients()
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]

        assert len(fillings) == 3
        assert fillings[0].get_name() == "cutlet"
        assert fillings[0].get_price() == 100
        assert fillings[1].get_name() == "dinosaur"
        assert fillings[1].get_price() == 200
        assert fillings[2].get_name() == "sausage"
        assert fillings[2].get_price() == 300

    def test_available_buns_returns_list(self):
        """Тест, что метод available_buns возвращает список"""
        buns = self.database.available_buns()

        assert type(buns) is list
        assert len(buns) == 3

    def test_available_ingredients_returns_list(self):
        """Тест, что метод available_ingredients возвращает список"""
        ingredients = self.database.available_ingredients()

        assert type(ingredients) is list
        assert len(ingredients) == 6
