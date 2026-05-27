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
    def test_ingredient_creation(self, ingredient_type, name, price):
        """Тест создания ингредиента с разными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_get_type(self):
        """Тест получения типа ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_ingredient_get_name(self):
        """Тест получения названия ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)

        assert ingredient.get_name() == "cutlet"

    @pytest.mark.parametrize("price", [0, 50.0, 100.0, 999.99])
    def test_ingredient_price_various_values(self, price):
        """Тест получения цены ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", price)

        assert ingredient.get_price() == price

    def test_ingredient_with_mock(self):
        """Тест с использованием мока"""
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "sauce"
        mock_ingredient.get_price.return_value = 150.00
        mock_ingredient.get_type.return_value = 'SAUCE'

        assert mock_ingredient.get_name() == "sauce"
        assert mock_ingredient.get_price() == 150.00
        assert mock_ingredient.get_type() == INGREDIENT_TYPE_SAUCE
