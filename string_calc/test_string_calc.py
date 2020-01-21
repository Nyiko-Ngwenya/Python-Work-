from calc import Add

import pytest

def test_adding_empty_string():
    
    assert Add('') == 0
    assert Add("1") == 1
    assert Add("1,1") == 2
    assert Add("1,2,3,4") == 10
    assert Add("1\n2,3" ) == 6
    assert Add("//;\n1;2") == 3
    assert Add("//4\n142") == 3
    assert Add("//***\n1***2***3") == 6
    assert Add("//[:D][%]\n1:D2%3") == 6
    assert Add("//[***][%%%]\n1***2%%%3") == 6
    assert Add("//[(-_-')][%]\n1(-_-')2%3") == 6
    assert Add("//[abc][777][:(]\n1abc27773:(1") == 7


