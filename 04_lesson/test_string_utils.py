import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected



class TestContains:
    """Тесты для метода contains"""
    
    # Позитивные тесты - символ существует
    def test_contains_positive_single_char(self):
        """Позитивные тесты: один символ"""
        assert mark.contains("SkyPro", "S") == True
        assert mark.contains("SkyPro", "k") == True
        assert mark.contains("SkyPro", "o") == True
        assert mark.contains("123", "2") == True
    
    def test_contains_positive_substring(self):
        """Позитивные тесты: подстрока"""
        assert utils.contains("SkyPro", "Pro") == True
        assert utils.contains("Hello World", "World") == True
        assert utils.contains("04 апреля 2023", "апреля") == True
    
    def test_contains_positive_special_chars(self):
        """Позитивные тесты: специальные символы"""
        assert utils.contains("Hello World", " ") == True
        assert utils.contains("test!@#", "!") == True
        assert utils.contains("a b c", " ") == True
    
    # Негативные тесты - символ не существует
    def test_contains_negative_not_found(self):
        """Негативные тесты: символ не найден"""
        assert utils.contains("SkyPro", "U") == False
        assert utils.contains("Hello", "x") == False
        assert utils.contains("123", "4") == False
    
    def test_contains_negative_case_sensitive(self):
        """Негативные тесты: регистрозависимость"""
        assert utils.contains("SkyPro", "s") == False
        assert utils.contains("SkyPro", "p") == False
        assert utils.contains("SkyPro", "PRO") == False
    
    def test_contains_negative_empty_cases(self):
        """Негативные тесты: пустые строки"""
        assert utils.contains("", "a") == False
        assert utils.contains(" ", "a") == False
        assert utils.contains("test", " ") == False
    
    def test_contains_edge_cases(self):
        """Граничные случаи"""
        assert utils.contains("a", "a") == True
        assert utils.contains("a", "b") == False
        assert utils.contains("", "") == True  # пустая строка содержит пустую подстроку
        assert utils.contains("test", "") == True  # любая строка содержит пустую подстроку
    
    def test_contains_negative_none(self):
        """Негативные тесты: None"""
        with pytest.raises(AttributeError):
            utils.contains(None, "a")
        with pytest.raises(TypeError):
            utils.contains("test", None)


class TestDeleteSymbol:
   @pytest.mark.positive
   def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
    # Позитивные проверки:
    assert string_utils.delete_symbol("skypro", "s") == "skypro"
    # Негативные проверки:
    assert string_utils.delete_symbol("skypro", "s") == "skypro"