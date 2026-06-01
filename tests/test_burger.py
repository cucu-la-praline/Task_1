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

    # ТЕСТЫ ДЛЯ МЕТОДА set_buns()

    def test_set_buns_set_bun_correctly(self):
        """Юнит Тест метода set_buns(): проверка установки булочки"""
        self.burger.set_buns(self.bun)
        assert self.burger.bun == self.bun

    def test_set_buns_bun_has_correct_name(self):
        """Юнит Тест метода set_buns(): проверка имени установленной булочки"""
        self.burger.set_buns(self.bun)
        assert self.burger.bun.get_name() == "test bun"

    def test_set_buns_bun_has_correct_price(self):
        """Юнит Тест метода set_buns(): проверка цены установленной булочки"""
        self.burger.set_buns(self.bun)
        assert self.burger.bun.get_price() == 100.0

    # ТЕСТЫ ДЛЯ МЕТОДА add_ingredient()

    def test_add_ingredient_increases_list_length(self):
        """Юнит Тест метода add_ingredient(): проверка увеличения списка"""
        self.burger.add_ingredient(self.ingredient1)
        assert len(self.burger.ingredients) == 1

    def test_add_ingredient_adds_correct_element(self):
        """Юнит Тест метода add_ingredient(): проверка добавления правильного ингредиента"""
        self.burger.add_ingredient(self.ingredient1)
        assert self.burger.ingredients[0] == self.ingredient1

    @pytest.mark.parametrize("ingredients_count", [1, 2, 3, 5])
    def test_add_multiple_ingredients(self, ingredients_count):
        """Юнит Тест добавления нескольких ингредиентов с параметризацией"""
        ingredients = [Mock(spec=Ingredient) for _ in range(ingredients_count)]

        for ingredient in ingredients:
            self.burger.add_ingredient(ingredient)

        assert len(self.burger.ingredients) == ingredients_count

    # ТЕСТЫ ДЛЯ МЕТОДА remove_ingredient()

    def test_remove_ingredient_deletes_element_at_valid_index(self):
        """Юнит Тест метода remove_ingredient(): удаление по валидному индексу"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        self.burger.remove_ingredient(0)

        assert len(self.burger.ingredients) == 1

    def test_remove_ingredient_remaining_element_is_correct(self):
        """Юнит Тест метода remove_ingredient(): проверка оставшегося элемента"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        self.burger.remove_ingredient(0)

        assert self.burger.ingredients[0] == self.ingredient2

    # ТЕСТЫ ДЛЯ МЕТОДА move_ingredient()

    def test_move_ingredient_first_element_moves_to_second_position(self):
        """Юнит Тест метода move_ingredient(): первый элемент перемещается на вторую позицию"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        self.burger.move_ingredient(0, 1)

        assert self.burger.ingredients[1] == self.ingredient1

    def test_move_ingredient_second_element_moves_to_first_position(self):
        """Юнит Тест метода move_ingredient(): второй элемент перемещается на первую позицию"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        self.burger.move_ingredient(1, 0)

        assert self.burger.ingredients[0] == self.ingredient2

    # ТЕСТЫ ДЛЯ МЕТОДА get_price()

    def test_get_price_returns_sum_with_bun_and_ingredients(self):
        """Юнит Тест метода get_price(): расчет цены с булочкой и ингредиентами"""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        expected_price = 200.0 + 50.0 + 75.0
        assert self.burger.get_price() == expected_price

    # ТЕСТЫ ДЛЯ МЕТОДА get_receipt()

    def test_get_receipt_contains_bun_name(self):
        """Юнит Тест метода get_receipt(): чек содержит название булочки"""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)

        receipt = self.burger.get_receipt()
        assert "(==== test bun ====)" in receipt

    def test_get_receipt_contains_ingredient_info(self):
        """Юнит Тест метода get_receipt(): чек содержит информацию об ингредиенте"""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)

        receipt = self.burger.get_receipt()
        assert "= sauce sauce1 =" in receipt

    def test_get_receipt_contains_multiple_ingredients(self):
        """Юнит Тест метода get_receipt(): чек содержит все ингредиенты"""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        receipt = self.burger.get_receipt()
        assert "= filling filling1 =" in receipt

    def test_get_receipt_contains_total_price(self):
        """Юнит Тест метода get_receipt(): чек содержит общую цену"""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        receipt = self.burger.get_receipt()
        assert "Price: 325.0" in receipt
