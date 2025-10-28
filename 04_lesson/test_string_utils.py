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
        assert utils.contains("SkyPro", "S") == True
        assert utils.contains("SkyPro", "k") == True
        assert utils.contains("SkyPro", "o") == True
        assert utils.contains("123", "2") == True
    
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
    """Тесты для метода delete_symbol"""
    
    # Позитивные тесты
    def test_delete_symbol_positive_single_char(self):
        """Позитивные тесты: один символ"""
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("Hello", "l") == "Heo"
        assert utils.delete_symbol("banana", "a") == "bnn"
    
    def test_delete_symbol_positive_substring(self):
        """Позитивные тесты: подстрока"""
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert utils.delete_symbol("Hello World", "World") == "Hello "
        assert utils.delete_symbol("04 апреля 2023", "апреля ") == "04 2023"
    
    def test_delete_symbol_positive_special_chars(self):
        """Позитивные тесты: специальные символы"""
        assert utils.delete_symbol("Hello World", " ") == "HelloWorld"
        assert utils.delete_symbol("test!@#", "!") == "test@#"
        assert utils.delete_symbol("a b c", " ") == "abc"
    
    def test_delete_symbol_positive_all_occurrences(self):
        """Позитивные тесты: все вхождения"""
        assert utils.delete_symbol("aaa", "a") == ""
        assert utils.delete_symbol("test test", "t") == "es es"
        assert utils.delete_symbol("ababab", "ab") == ""
    
    # Негативные тесты
    def test_delete_symbol_negative_not_found(self):
        """Негативные тесты: символ не найден"""
        assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
        assert utils.delete_symbol("Hello", "x") == "Hello"
        assert utils.delete_symbol("test", "xyz") == "test"
    
    def test_delete_symbol_negative_empty_cases(self):
        """Негативные тесты: пустые строки"""
        assert utils.delete_symbol("", "a") == ""
        assert utils.delete_symbol(" ", " ") == ""
        assert utils.delete_symbol("test", "") == "test"
    
    def test_delete_symbol_negative_case_sensitive(self):
        """Негативные тесты: регистрозависимость"""
        assert utils.delete_symbol("SkyPro", "s") == "SkyPro"
        assert utils.delete_symbol("SkyPro", "PRO") == "SkyPro"
    
    def test_delete_symbol_edge_cases(self):
        """Граничные случаи"""
        assert utils.delete_symbol("", "") == ""  # удаление пустой строки из пустой
        assert utils.delete_symbol("aaaa", "aa") == ""  # перекрывающиеся подстроки
    
    def test_delete_symbol_negative_none(self):
        """Негативные тесты: None"""
        with pytest.raises(AttributeError):
            utils.delete_symbol(None, "a")
        with pytest.raises(TypeError):
            utils.delete_symbol("test", None)
