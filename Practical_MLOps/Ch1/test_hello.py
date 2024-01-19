import numpy as np 
from hello import add, numpy_add


def test_add():
    assert 2 == add(1, 1)
    
def test_numpy_add():
    assert 1 == 1