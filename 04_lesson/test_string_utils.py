import pytest
from string_utils import StringUtils

utils = StringUtils()

class TestCapitalize:

    # Позитивные тесты
    def test_capitalize_positive_common_cases(self):
       
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hello world") == "Hello world"
        assert utils.capitalize("python") == "Python"
    
    def test_capitalize_positive_special_cases(self):
        
        assert utils.capitalize("a") == "A"  # одна буква
        assert utils.capitalize("123abc") == "123abc"  # цифры в начале
        assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"  # строка с пробелами и цифрами
        assert utils.capitalize("тест") == "Тест"  # кириллица
    
    # Негативные тесты
    def test_capitalize_negative_empty_string(self):
       
        assert utils.capitalize("") == ""
    
    def test_capitalize_negative_spaces(self):
       
        assert utils.capitalize(" ") == " "
        assert utils.capitalize("   ") == "   "
    
class TestTrim:
   
    # Позитивные тесты
    def test_trim_positive_common_cases(self):
        
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("  hello") == "hello"
        assert utils.trim(" test") == "test"
        assert utils.trim("   04 апреля 2023") == "04 апреля 2023"
    
    # Негативные тесты
    def test_trim_negative_empty_string(self):
        """Негативные тесты: пустая строка"""
        assert utils.trim("") == ""
    
    
    def test_trim_negative_none(self):
      
        with pytest.raises(AttributeError):
            utils.trim(None)


class TestContains:
    
    # Позитивные тесты - символ существует
    def test_contains_positive_single_char(self):
       
        assert utils.contains("SkyPro", "S") == True
        assert utils.contains("SkyPro", "k") == True
        assert utils.contains("SkyPro", "o") == True
        assert utils.contains("123", "2") == True
    
    # Негативные тесты - символ не существует
    def test_contains_negative_not_found(self):
       
        assert utils.contains("SkyPro", "U") == False
        assert utils.contains("Hello", "x") == False
        assert utils.contains("123", "4") == False
    
    
    def test_contains_negative_empty_cases(self):
      
        assert utils.contains("", "a") == False
        assert utils.contains(" ", "a") == False
        assert utils.contains("test", " ") == False
       
class TestDeleteSymbol:
    
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
    
    
