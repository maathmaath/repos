import pytest
import json

# @pytest.fixture
# def input_value():
#    input = 39
#    return input


@pytest.fixture
def input_dict():
    j = {}
    with open('make_model.json', 'r') as f:
        j = json.load(f)
    make_model_dict = dict(j)
    L = []
    for i in make_model_dict:
        L.append((i, make_model_dict[i]))
    return L
