from monty.operator import operator_from_str


class TestOperator:
    def test_something(self):
        assert operator_from_str("==")(1, 1) and operator_from_str("+")(1, 1) == 2
