""" Test vscode-python issue 3869: https://github.com/Microsoft/vscode-python/issues/3869 """

import pytest

def test_does_not_set_breakpoints():

    fails_misserably = "hu hu"
    
    assert fails_misserably
