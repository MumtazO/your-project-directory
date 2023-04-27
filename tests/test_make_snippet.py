from lib.make_snippet import *

def test_make_snippet():
    result = make_snippet("this should be a long long string")
    assert result == "this should be a long..."


def test_make_snippet_second():
    result = make_snippet("this should be a huge red train")
    assert result == "this should be a huge..."

def test_make_snippet_short():
    result = make_snippet("hello world snippet")
    assert result == "hello world snippet"