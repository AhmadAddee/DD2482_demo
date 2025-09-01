from src.sut import str_ops

def test_sanitize():
    assert str_ops.sanitize(" HeLLo WoRLD ") == "hello world"

def test_slugify():
    assert str_ops.slugify("Hello, World!") == "hello-world"

def test_palindrome_true():
    assert str_ops.is_palindrome("A man, a plan, a canal: Panama")

def test_word_count():
    assert str_ops.word_count("a A a b") == {"a": 3, "b": 1}