import pytest
from string_utils import StringUtils

utils = StringUtils()

class TestCapitalize:
    """Тесты для метода capitalize"""
    
    # Позитивные тесты
    def test_capitalize_positive_common_cases(self):
        """Позитивные тесты: обычные случаи"""
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hello world") == "Hello world"
        assert utils.capitalize("python") == "Python"
    
    def test_capitalize_positive_special_cases(self):
        """Позитивные тесты: специальные случаи"""
        assert utils.capitalize("a") == "A"  # одна буква
        assert utils.capitalize("123abc") == "123abc"  # цифры в начале
        assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"  # строка с пробелами и цифрами
        assert utils.capitalize("тест") == "Тест"  # кириллица
    
    # Негативные тесты
    def test_capitalize_negative_empty_string(self):
        """Негативные тесты: пустая строка"""
        assert utils.capitalize("") == ""
    
    def test_capitalize_negative_spaces(self):
        """Негативные тесты: пробелы"""
        assert utils.capitalize(" ") == " "
        assert utils.capitalize("   ") == "   "
    
    def test_capitalize_negative_already_capitalized(self):
        """Негативные тесты: уже заглавная первая буква"""
        assert utils.capitalize("Skypro") == "Skypro"
        assert utils.capitalize("Test") == "Test"
    
    def test_capitalize_negative_special_characters(self):
        """Негативные тесты: специальные символы"""
        assert utils.capitalize("!test") == "!test"
        assert utils.capitalize("@hello") == "@hello"
        assert utils.capitalize("123") == "123"
    
    def test_capitalize_negative_none(self):
        """Негативные тесты: None"""
        with pytest.raises(AttributeError):
            utils.capitalize(None)


class TestTrim:
    """Тесты для метода trim"""
    
    # Позитивные тесты
    def test_trim_positive_common_cases(self):
        """Позитивные тесты: обычные случаи"""
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("  hello") == "hello"
        assert utils.trim(" test") == "test"
        assert utils.trim("   04 апреля 2023") == "04 апреля 2023"
    
    def test_trim_positive_multiple_spaces(self):
        """Позитивные тесты: множественные пробелы"""
        assert utils.trim("     multiple") == "multiple"
        assert utils.trim("  a") == "a"
    
    # Негативные тесты
    def test_trim_negative_empty_string(self):
        """Негативные тесты: пустая строка"""
        assert utils.trim("") == ""
    
    def test_trim_negative_only_spaces(self):
        """Негативные тесты: только пробелы"""
        assert utils.trim(" ") == ""
        assert utils.trim("   ") == ""
        assert utils.trim("      ") == ""
    
    def test_trim_negative_no_leading_spaces(self):
        """Негативные тесты: нет начальных пробелов"""
        assert utils.trim("skypro") == "skypro"
        assert utils.trim("skypro   ") == "skypro   "
        assert utils.trim("hello world") == "hello world"
    
    def test_trim_negative_mixed_spaces(self):
        """Негативные тесты: пробелы в середине и конце"""
        assert utils.trim("sky pro") == "sky pro"
        assert utils.trim("  hello  world  ") == "hello  world  "
    
    def test_trim_negative_none(self):
        """Негативные тесты: None"""
        with pytest.raises(AttributeError):
            utils.trim(None)


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


class TestIntegration:
    """Интеграционные тесты - проверка комбинаций методов"""
    
    def test_trim_and_capitalize(self):
        """Тест комбинации trim + capitalize"""
        result = utils.capitalize(utils.trim("   hello world"))
        assert result == "Hello world"
    
    def test_contains_and_delete(self):
        """Тест комбинации contains + delete_symbol"""
        text = "Hello World"
        if utils.contains(text, "World"):
            result = utils.delete_symbol(text, "World")
            assert result == "Hello "
    
    def test_multiple_operations(self):
        """Тест множественных операций"""
        text = "   multiple   test   "
        trimmed = utils.trim(text)
        capitalized = utils.capitalize(trimmed)
        cleaned = utils.delete_symbol(capitalized, "   ")
        
        assert trimmed == "multiple   test   "
        assert capitalized == "Multiple   test   "
        assert cleaned == "Multiple test"
    
    def test_complex_scenario(self):
        """Комплексный сценарий"""
        text = "   remove spaces and capitalize first letter   "
        
        # Удаляем начальные пробелы
        step1 = utils.trim(text)
        assert step1 == "remove spaces and capitalize first letter   "
        
        # Делаем первую букву заглавной
        step2 = utils.capitalize(step1)
        assert step2 == "Remove spaces and capitalize first letter   "
        
        # Проверяем наличие пробелов
        assert utils.contains(step2, " ") == True
        
        # Удаляем все пробелы
        step3 = utils.delete_symbol(step2, " ")
        assert step3 == "Removespacesandcapitalizefirstletter   "
        
        # Удаляем оставшиеся пробелы в конце
        step4 = utils.delete_symbol(step3, " ")
        assert step4 == "Removespacesandcapitalizefirstletter"


class TestPerformanceAndSpecial:
    """Тесты производительности и специальных случаев"""
    
    def test_long_strings(self):
        """Тесты с длинными строками"""
        long_text = "a" * 1000 + "TARGET" + "b" * 1000
        result = utils.delete_symbol(long_text, "TARGET")
        assert result == "a" * 1000 + "b" * 1000
        assert utils.contains(long_text, "TARGET") == True
        assert utils.contains(result, "TARGET") == False
    
    def test_unicode_characters(self):
        """Тесты с Unicode символами"""
        assert utils.capitalize("café") == "Café"
        assert utils.trim("   café") == "café"
        assert utils.contains("café", "é") == True
        assert utils.delete_symbol("café", "é") == "caf"
    
    def test_numbers_as_strings(self):
        """Тесты с числами как строками"""
        assert utils.capitalize("123") == "123"
        assert utils.trim("   456") == "456"
        assert utils.contains("123", "2") == True
        assert utils.delete_symbol("12345", "3") == "1245"