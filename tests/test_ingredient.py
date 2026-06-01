import pytest

from unittest.mock import Mock
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 150.0),
        (INGREDIENT_TYPE_FILLING, "cheese", 80.5),
        ("UNKNOWN_TYPE", "special", 300.0)
    ])
    def test_ingredient_creation_sets_type_correctly(self, ingredient_type, name, price):
        """
        Тест конструктора ингредиента: проверка установки типа
        """
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 150.0),
        (INGREDIENT_TYPE_FILLING, "cheese", 80.5),
        ("UNKNOWN_TYPE", "special", 300.0)
    ])
    def test_ingredient_creation_sets_name_correctly(self, ingredient_type, name, price):
        """
        Тест конструктора ингредиента: проверка установки названия
        """
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 150.0),
        (INGREDIENT_TYPE_FILLING, "cheese", 80.5),
        ("UNKNOWN_TYPE", "special", 300.0)
    ])
    def test_ingredient_creation_sets_price_correctly(self, ingredient_type, name, price):
        """
        Тест конструктора ингредиента: проверка установки цены
        """
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    def test_ingredient_get_type(self):
        """Тест получения типа ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_type_returns_string(self):
        """
        Тест метода get_type(): проверка типа возвращаемого значения
        """
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert type(ingredient.get_type()) is str

    def test_ingredient_get_name(self):
        """Тест получения названия ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)

        assert ingredient.get_name() == "cutlet"

    def test_get_name_returns_string(self):
        """
        Тест метода get_name(): проверка типа возвращаемого значения
        """
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert type(ingredient.get_name()) is str

    @pytest.mark.parametrize("price", [0, 50.0, 100.0, 999.99])
    def test_ingredient_price_various_values(self, price):
        """Тест получения цены ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", price)

        assert ingredient.get_price() == price

    def test_mock_ingredient_get_name_returns_mocked_value(self):
        """
        Тест с использованием мока: проверка метода get_name()
        """
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "mocked sauce"

        assert mock_ingredient.get_name() == "mocked sauce"

    def test_mock_ingredient_get_price_returns_mocked_value(self):
        """
        Тест с использованием мока: проверка метода get_price()
        """
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 999.99

        assert mock_ingredient.get_price() == 999.99

    def test_mock_ingredient_get_type_returns_mocked_value(self):
        """
        Тест с использованием мока: проверка метода get_type()
        """
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE

        assert mock_ingredient.get_type() == INGREDIENT_TYPE_SAUCE
