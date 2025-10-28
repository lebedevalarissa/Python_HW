import pytest
from string_utils import StringUtils

class TestStringUtils:
    
    @pytest.fixture
    def utils(self):
        return StringUtils()
    
    # Тесты для capitalize
    def test_capitalize_positive(self, utils):
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hello world") == "Hello world"
        assert utils.capitalize("123abc") == "123abc"
    
    def test_capitalize_negative(self, utils):
        assert utils.capitalize("") == ""
        assert utils.capitalize(" ") == " "
        assert utils.capitalize(None) is None
        assert utils.capitalize("SkyPro") == "SkyPro"
    
    # Тесты для trim
    def test_trim_positive(self, utils):
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("  hello  ") == "hello  "
        assert utils.trim("skypro") == "skypro"
    
    def test_trim_negative(self, utils):
        assert utils.trim("") == ""
        assert utils.trim(" ") == ""
        assert utils.trim(None) is None
    
    # Тесты для to_list
    def test_to_list_positive(self, utils):
        assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
        assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
        assert utils.to_list("apple") == ["apple"]
    
    def test_to_list_negative(self, utils):
        assert utils.to_list("") == []
        assert utils.to_list(" ") == [" "]
        assert utils.to_list(None) == []
        assert utils.to_list("a,,b") == ["a", "", "b"]
    
    # Тесты для contains
    def test_contains_positive(self, utils):
        assert utils.contains("SkyPro", "S") == True
        assert utils.contains("SkyPro", "Pro") == True
        assert utils.contains("Hello World", " ") == True
    
    def test_contains_negative(self, utils):
        assert utils.contains("SkyPro", "U") == False
        assert utils.contains("", "a") == False
        assert utils.contains(" ", "a") == False
        assert utils.contains(None, "a") == False
        assert utils.contains("SkyPro", None) == False
    
    # Тесты для delete_symbol
    def test_delete_symbol_positive(self, utils):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert utils.delete_symbol("Hello World", " ") == "HelloWorld"
    
    def test_delete_symbol_negative(self, utils):
        assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
        assert utils.delete_symbol("", "a") == ""
        assert utils.delete_symbol(None, "a") is None
        assert utils.delete_symbol("SkyPro", None) == "SkyPro"
    
    # Тесты для starts_with
    def test_starts_with_positive(self, utils):
        assert utils.starts_with("SkyPro", "S") == True
        assert utils.starts_with("123abc", "123") == True
        assert utils.starts_with(" Hello", " ") == True
    
    def test_starts_with_negative(self, utils):
        assert utils.starts_with("SkyPro", "P") == False
        assert utils.starts_with("", "a") == False
        assert utils.starts_with(" ", "a") == False
        assert utils.starts_with(None, "a") == False
        assert utils.starts_with("SkyPro", None) == False
    
    # Тесты для end_with
    def test_end_with_positive(self, utils):
        assert utils.end_with("SkyPro", "o") == True
        assert utils.end_with("abc123", "123") == True
        assert utils.end_with("Hello ", " ") == True
    
    def test_end_with_negative(self, utils):
        assert utils.end_with("SkyPro", "y") == False
        assert utils.end_with("", "a") == False
        assert utils.end_with(" ", "a") == False
        assert utils.end_with(None, "a") == False
        assert utils.end_with("SkyPro", None) == False
    
    # Тесты для is_empty
    def test_is_empty_positive(self, utils):
        assert utils.is_empty("") == True
        assert utils.is_empty(" ") == True
        assert utils.is_empty("  ") == True
    
    def test_is_empty_negative(self, utils):
        assert utils.is_empty("SkyPro") == False
        assert utils.is_empty("  hello  ") == False
        assert utils.is_empty("123") == False
        assert utils.is_empty(None) == True
    
    # Тесты для list_to_string
    def test_list_to_string_positive(self, utils):
        assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
        assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
        assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    
    def test_list_to_string_negative(self, utils):
        assert utils.list_to_string([]) == ""
        assert utils.list_to_string([""]) == ""
        assert utils.list_to_string(None) == ""
        assert utils.list_to_string(["a", "", "c"]) == "a, , c"