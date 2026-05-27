import pytest

from bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100.0),
        ("white bun", 150.5),
        ("sesame bun", 200.0),
        ("", 0.0),
        ("luxury bun", 99999.99)
    ])
    def test_get_name(self, name, price):
        """Тест создания булочки с разными параметрами"""
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_get_name(self):
        """Тест получения названия булочки"""
        bun = Bun("classic bun", 120.0)

        assert bun.get_name() == "classic bun"
        assert type(bun.get_name()) is str

    def test_bun_get_price(self):
        """Тест получения цены булочки"""
        bun = Bun("classic bun", 120.0)

        assert bun.get_price() == 120.0
        assert type(bun.get_price()) is float

    @pytest.mark.parametrize("price", [0.01, 50.0, 100.0, 1000.0])
    def test_bun_price_types(self, price):
        """Тест разных значений цены"""
        bun = Bun("test bun", price)

        assert bun.get_price() == price
