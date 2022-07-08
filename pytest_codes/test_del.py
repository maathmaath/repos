import pytest
import json
import del_a as a


# @pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44)])
# def test_multiplication_11(num, output):
#     assert 11*num == output


def attr():
    return a.input_dict()


class TestPrinter:

    @pytest.mark.parametrize("make, model", attr())
    def test_call_addPrinter(self, make, model):
        assert make == model

    # @pytest.mark.parametrize()
    # def test_call_deletePrinter():
    #     print()
