import pytest


@pytest.mark.parametrize('common_arg1', [0, 1])
@pytest.mark.parametrize('common_arg2', [2, 3])
class TestParametrized:

    @pytest.mark.parametrize('a', [0, 2])
    def test_1(self, common_arg1, common_arg2, a):
        assert common_arg1 == a
        assert common_arg2 == a

    @pytest.mark.parametrize('b', [1, 3])
    def test_2(self, common_arg1, common_arg2, b):
        assert common_arg1 == b
        assert common_arg2 == b

    @pytest.mark.parametrize('x', [0, 3])
    def test_100(self, common_arg1, common_arg2, x):
        assert common_arg1 == x
        assert common_arg2 == x
