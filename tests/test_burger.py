import pytest
from unittest.mock import Mock

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def setup_method(self):
        """Подготовка данных для каждого теста"""
        self.burger = Burger()
        self.bun = Mock(spec=Bun)
        self.bun.get_name.return_value = "test bun"
        self.bun.get_price.return_value = 100.0

        self.ingredient1 = Mock(spec=Ingredient)
        self.ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        self.ingredient1.get_name.return_value = "sauce1"
        self.ingredient1.get_price.return_value = 50.0

        self.ingredient2 = Mock(spec=Ingredient)
        self.ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        self.ingredient2.get_name.return_value = "filling1"
        self.ingredient2.get_price.return_value = 75.0

    def test_set_buns(self):
        """Тест установки булочки"""
        self.burger.set_buns(self.bun)

        assert self.burger.bun == self.bun
        assert self.burger.bun.get_name() == "test bun"
        assert self.burger.bun.get_price() == 100.0

    def test_add_ingredient(self):
        """Тест добавления ингредиента"""
        self.burger.add_ingredient(self.ingredient1)

        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.ingredient1

    @pytest.mark.parametrize("ingredients_count", [1, 2, 3, 5])
    def test_add_multiple_ingredients(self, ingredients_count):
        """Тест добавления нескольких ингредиентов с параметризацией"""
        ingredients = [Mock(spec=Ingredient) for _ in range(ingredients_count)]

        for ingredient in ingredients:
            self.burger.add_ingredient(ingredient)

        assert len(self.burger.ingredients) == ingredients_count

    def test_remove_ingredient_valid_index(self):
        """Тест удаления ингредиента по валидному индексу"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        self.burger.remove_ingredient(0)

        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.ingredient2

    def test_move_ingredient(self):
        """Тест перемещения ингредиента"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        self.burger.move_ingredient(0, 1)

        assert self.burger.ingredients[0] == self.ingredient2
        assert self.burger.ingredients[1] == self.ingredient1

    def test_get_price_with_bun_and_ingredients(self):
        """Тест расчета цены с булочкой и ингредиентами"""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        expected_price = (100.0 * 2) + 50.0 + 75.0
        assert self.burger.get_price() == expected_price

    def test_get_receipt_with_bun_and_ingredients(self):
        """Тест получения чека с булочкой и ингредиентами"""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        receipt = self.burger.get_receipt()

        assert "(==== test bun ====)" in receipt
        assert "= sauce sauce1 =" in receipt
        assert "= filling filling1 =" in receipt
        assert "Price: 325.0" in receipt