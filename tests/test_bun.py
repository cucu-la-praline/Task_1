import pytest

from bun import Bun


class TestBun:
    def test_bun_get_name(self):
        """Юнит Тест получения названия булочки"""
        bun = Bun("classic bun", 120.0)
        assert bun.get_name() == "classic bun"

    def test_get_name_returns_string(self):
        """Юнит Тест метода get_name(): проверка типа возвращаемого значения"""
        bun = Bun("classic bun", 120.0)
        assert type(bun.get_name()) is str

    def test_get_price_returns_float(self):
        """Юнит Тест метода get_price(): проверка типа возвращаемого значения"""
        bun = Bun("classic bun", 120.0)
        assert type(bun.get_price()) is float

    @pytest.mark.parametrize("price", [0.01, 50.0, 100.0, 1000.0])
    def test_bun_get_price(self, price):
        """Юнит Тест получения цены булочки"""
        bun = Bun("test bun", price)
        assert bun.get_price() == price
