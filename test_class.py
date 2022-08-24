"""
Run pytest in environment. 

Test all files with test_*.py or *_test.py
$pytest 

Test specific file
$pytest test_class.py

Test by keyword. Test MyClass but not method with name test_method_example()
$pytest -k "MyClass and not method"
"""

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4