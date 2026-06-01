import pytest

from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def setup_method(self):
        """Подготовка данных для каждого теста"""
        self.database = Database()

    def test_available_buns_returns_list(self):
        """Тест метода available_buns(): проверка типа возвращаемого значения"""
        buns = self.database.available_buns()
        assert type(buns) is list

    def test_available_buns_returns_three_items(self):
        """Тест метода available_buns(): проверка количества булочек"""
        buns = self.database.available_buns()
        assert len(buns) == 3

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_available_buns_bun_parameters_name(self, index, expected_name, expected_price):
        """Параметризованный тест для проверки названия всех булочек"""
        buns = self.database.available_buns()
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_available_buns_bun_parameters_price(self, index, expected_name, expected_price):
        """Параметризованный тест для проверки це н всех булочек"""
        buns = self.database.available_buns()
        assert buns[index].get_price() == expected_price

    def test_available_ingredients_returns_list(self):
        """Тест метода available_ingredients(): проверка типа возвращаемого значения"""
        ingredients = self.database.available_ingredients()
        assert type(ingredients) is list

    def test_available_ingredients_returns_six_items(self):
        """Тест метода available_ingredients(): проверка количества ингридиентов"""
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6

    def test_database_has_three_sauces(self):
        """Тест метода available_ingredients(): проверка количества соусов"""
        ingredients = self.database.available_ingredients()
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "hot sauce", 100),
        (1, "sour cream", 200),
        (2, "chili sauce", 300)
    ])
    def test_sauce_parameters_name(self, index, expected_name, expected_price):
        """Параметризованный тест для проверки всех соусов"""
        ingredients = self.database.available_ingredients()
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert sauces[index].get_name() == expected_name

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "hot sauce", 100),
        (1, "sour cream", 200),
        (2, "chili sauce", 300)
    ])
    def test_sauce_parameters_price(self, index, expected_name, expected_price):
        """Параметризованный тест для проверки всех соусов"""
        ingredients = self.database.available_ingredients()
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert sauces[index].get_price() == expected_price

    def test_database_has_three_fillings(self):
        """Тест метода available_ingredients(): проверка количества начинок"""
        ingredients = self.database.available_ingredients()
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "cutlet", 100),
        (1, "dinosaur", 200),
        (2, "sausage", 300)
    ])
    def test_filling_parameters_name(self, index, expected_name, expected_price):
        """Параметризованный тест для проверки всех начинок"""
        ingredients = self.database.available_ingredients()
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert fillings[index].get_name() == expected_name

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "cutlet", 100),
        (1, "dinosaur", 200),
        (2, "sausage", 300)
    ])
    def test_filling_parameters_price(self, index, expected_name, expected_price):
        """Параметризованный тест для проверки всех начинок"""
        ingredients = self.database.available_ingredients()
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert fillings[index].get_price() == expected_price
